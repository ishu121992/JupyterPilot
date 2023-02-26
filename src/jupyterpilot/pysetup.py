import os
import openai
import time
import pkg_resources
from IPython.display import display, Code, clear_output

class CodetoCell:
    """
    This class is used to generate code from a prompt using OpenAI's Codex API.
    The code is then saved to a file and loaded in jupyter notebook. It will not work in other IDEs.

    Parameters
    ----------
    openai_key : str
        This is the OpenAI API key.
    response : str
        This is the response from the OpenAI API.
    model : str
        This is the model used to generate the code.
        default = "code-davinci-002"
        Other models can be found here: https://beta.openai.com/docs/engines/code-completion
        For example, "code-cushman-001" is almost as capable as "code-davinci-002" but is much faster. It has a maximum of 2048 tokens.

    tokens : int    
        This is the number of tokens used to generate the code. Default is 1000.
        The number of tokens can be increased to get more code.
        code-davinci-002 supports a maximum of 8,000 tokens.

    Methods
    -------
    get_code(prompt)
        This method is used to get the code and load it in jupyter notebook.

        Parameters
        ----------
        prompt : str
            This is the prompt used to generate the code.

    Examples
    --------
    from jupyterpilot import pysetup
    openai_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    codex = pysetup.CodetoCell(openai_key)
    codex.get_code(prompt="Create a function to convert speech to text using Google Speech to Text API.")

    use %load test.py to load the file in jupyter notebook
    """

    def __init__(self, openai_key, response=None, model="code-davinci-002",tokens=1000):
        self.response = response
        self.openai_key = openai_key
        self.model = model
        self.tokens = tokens

    # Get the response from the OpenAI API
    def get_model_response(self,prompt):
        self.response = openai.Completion.create(
            model=self.model,
            prompt=prompt,
            temperature=0,
            max_tokens=self.tokens,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0
            )
        return self.response
    
    # Parse the code from the response
    def code_parser_input(self,code_list):
        output = ''
        for line in code_list:
            if len(line) == 0:
                output = output+'\n'
            elif '%' in line:
                continue
            elif '#' in line:
                line = line[1:]
                output +=(line+'\n')
            else:
                output +=(line+'\n')
        return output
    
    # Parse the response from the OpenAI API
    def parse_response(self):
        code_to_parse = self.response['choices'][0]['text']
        c = code_to_parse.split('\n')
        imp_statements = [line for line in c if 'import' in line]
        code_to_ex = [line for line in c if line.find('import')]
        code_input_string = self.code_parser_input(code_to_ex)
        return imp_statements,code_input_string
    
    # Save the code to a file
    def save_code_to_file(self,code_input_string,imp_statements):
        fpath = os.path.join(os.getcwd(),'test.py')
        with open(fpath, 'w') as fp:
            pass
        with open('test.py', 'w') as f:
            for line in imp_statements:
                f.write(line)
                f.write('\n')
            for code_line in code_input_string:
                f.write(code_line)
        os.chmod(fpath, 0o755)

    # Load the file in jupyter notebook
    def load_test(self):
        fpath = os.path.join(os.getcwd(),'test.py')
        # Show loading message
        loading_msg = 'Loading'
        for i in range(3):
            clear_output(wait=True)
            display(f"{loading_msg}{'.' * i}")
            time.sleep(1)

        try:
            shell = get_ipython().__class__.__name__
            if shell == 'ZMQInteractiveShell':
                # Running in Jupyter notebook
                get_ipython().run_line_magic('load', fpath)
                clear_output()
            else:
                # Not running in Jupyter notebook
                print("Not running in Jupyter notebook.")
        except NameError:
            # get_ipython() not defined, not running in Jupyter notebook
            print("Not running in Jupyter notebook.")


    # get the code and load it in jupyter notebook
    def get_code(self,prompt):
        openai.api_key = self.openai_key
        self.get_model_response(prompt)
        imp_statements,code_input_string = self.parse_response()
        self.save_code_to_file(code_input_string,imp_statements)
        self.load_test()