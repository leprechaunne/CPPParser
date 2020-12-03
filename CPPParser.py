import re
import os
from collections import ChainMap

class CPPParser:
	"""
	The function of this class is to automatically parse given C++ code (Google styleguide) and turn it into a function (if
	it isn't already one) and add a skeleton of parameter definitions. The skeleton will look roughly like this:
		// 
		// `make_unique`
		// `i` 
		// `buffer_index`
		// `modified_buffer_index`
		// `num_bugs`
		util::StatusOr<std::unique_ptr<IOBuffer>> FunctionName(const int& buffer_index){
		        ...
		}
	"""
	reserved_keywords = ["alignas","alignof","and","and_eq","asm","atomic_cancel","atomic_commit","atomic_noexcept","auto","bitand","bitor","bool",
					"break","case","catch","char","char8_t","char16_t","char32_t","class","compl","concept","const","consteval","constexpr","constinit",
					"const_cast","continue","co_await","co_return","co_yield","decltype","default","define","defined","delete","do","double","dynamic_cast",
					"elif","else","endif","enum","error","explicit","export","extern","false","final","float","for","friend","goto","if","ifdef","ifndef",
					"inline","int","line","long","mutable","namespace","new","noexcept","not","not_eq","nullptr","operator","or","or_eq","override",
					"pragma","private","protected","public","register","reinterpret_cast","requires","return","short","signed","sizeof","static",
					"static_assert","static_cast","struct","switch","synchronized","template","this","thread_local","throw","transaction_safe",
					"transaction_safe_dynamic","true","try","typedef","typeid","typename","undef","union","unsigned","using","virtual","void",
					"volatile","wchar_t","while","xor","xor_eq"]

	# 'local_namespace_names'	- variable names that are defined within the block, not passed in
	# 'passed_in_names'			- variable names that are passed in through function parameters
	def __init__(self):
		self.local_namespace_names = {}
		self.passed_in_names = {}
		self.main()

	def main(self):	
		#clear screen
		os.system('cls' if os.name == 'nt' else 'clear')

		#save plaintext
		file = open("examplecode1.txt")
		self.plain_text = file.read()
		file.close()

		#tostring plain text
		# print(self.plain_text,"\n\n" + "-"*60 + "\n")

		#clean code up (but dont modify the plaintext, they probably like their code formatted like that)
		linter = CPP_Linter(self.plain_text)
		self.linted_code = linter.get_linted_code()

		#tostring print
		#print(self.linted_code)

		self.find_variables()

		self.generate_skeleton_comment()


	def find_variables(self):
		potential_variables = re.finditer("(?P<vartype>[a-zA-Z0-9\_\-]*)\s(?P<varname>[a-zA-Z0-9\_\-]*) ?=[^=]", self.linted_code)

		for var in potential_variables:
			var_name = var.group("varname")
			var_type = var.group("vartype")

			# print("name: {:30} type: {:20}".format(var_name, var_type))

			if self.is_variable_new_and_valid(var_name):
				self.local_namespace_names[var_name] = var_type
		# print(self.local_namespace_names)

	def generate_skeleton_comment(self):
		#LATER: format variables as table that adjusts based on longest variable name used'
		#		will need an import, because variable tables aren't possible in python
		self.skeleton_comment = "//"

		print(self.local_namespace_names)
		ten = 10
		for var_name, var_type in self.passed_in_names.items():
			#print table
			self.skeleton_comment += "\n//'{:35}{:10} - ".format(var_name+"'", var_type)

		for var_name, var_type in self.local_namespace_names.items():
			#print table
			self.skeleton_comment += "\n//'{:35}{:10} - ".format(var_name+"'", var_type) 

		print(self.skeleton_comment)

	def is_CPP_reserved_keyword(self, name):
		if name in CPPParser.reserved_keywords:
			return True
		return False

	def is_variable_already_known(self, name):
		#checks if a variable is already known
		if name in self.local_namespace_names:
			return True
		if name in self.passed_in_names:
			return True
		return False

	def is_variable_new_and_valid(self, name):
		if self.is_CPP_reserved_keyword(name) and self.is_variable_already_known(name):
			return False
		return True

class CPP_Linter:
	def __init__(self, unlinted_code):
		self.unlinted_code = unlinted_code
		self.lint_code()

	def lint_code(self):
		# 1. clear any whitespace before line breaks
		self.linted_code = re.sub(r"(\s)+[\r\n]", r"\r\n", self.unlinted_code)
		#print(self.linted_code, "\n\n" + "-"*60 + "\n")

		# 1.5. replace \r\n with \n
		self.linted_code = re.sub(r"\r\n", r"\n", self.linted_code)
		# print(self.linted_code, "\n\n" + "-"*60 + "\n")

		# 2. clear any line breaks that dont follow ';', '{', or '}'
		#		using raw strings because of the sheer amount of escaped characters
		self.linted_code = re.sub(r"([^;{}])[\r\n]+\s*", r"\1", self.linted_code)
		#print(self.linted_code, "\n\n" + "-"*60 + "\n")

	def get_linted_code(self):
		return self.linted_code

parser = CPPParser()