from itertools import chain

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
		self.local_namespace_names = []
		self.passed_in_names = []
		self.main()

	def main(self):
		file = open("vimscript.txt")
		file_lines = file.readlines()

		for line in file_lines:
			print(line)

	def generate_skeleton_comment(self):
		#LATER: format variables as table that adjusts based on longest variable name used
		for name in map(None, self.passed_in_names:
			#print table

		for name in self.local_namespace_names:
			#print table