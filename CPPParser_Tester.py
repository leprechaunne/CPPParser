from CPPParser import CPPParser, CPP_Linter

















# CPP_Linter tests

#CPP_Linter_Test_1
CPP_Linter_Test_1_Answer = """auto make_unique = absl::make_unique<std::unique_ptr<IOBuffer>>();
int i = 0;
for(int i = 0; i < 30; i++){
        if(i % 3 % 2 == 0){
                uint64 modified_buffer_index = 12343 * i;
                const int num_bugs = LOGBUG.count();
                RETURN_IF_ERROR(LoadBuffer(buffer_index));
                LOG_BUG(num_bugs, modified_buffer_index);
        }
}
return make_unique;"""

def CPP_Linter_Test_1():
	#Basic given example
	file = open("examplecode1.txt")
	test_string = file.read()
	file.close()

	answer = CPP_Linter(test_string)
	assert answer.get_linted_code() == CPP_Linter_Test_1_Answer

#CPP_Linter_Test_2
CPP_Linter_Test_2_Answer = r"""this line is okay;
this line is not okay{}
this line is also not okay(this, is not,okay);
also this}"""

def CPP_Linter_Test_2():
	#Basic english example
	file = open("examplecode2.txt")
	test_string = file.read()
	file.close()

	answer = CPP_Linter(test_string)
	assert answer.get_linted_code() == CPP_Linter_Test_2_Answer

#CPP_Linter_Test_3
CPP_Linter_Test_3_Answer = r"""ClassName obj;
ClassName obj2(param1, param2);
auto OBJ3 = ClassName(parameter2=param2);
if(elems[i] = true){
	ClassName obj_4(param1,param2,param3);
}"""

def CPP_Linter_Test_3():
		#Basic english example
	file = open("examplecode3.txt")
	test_string = file.read()
	file.close()

	answer = CPP_Linter(test_string)
	assert answer.get_linted_code() == CPP_Linter_Test_3_Answer