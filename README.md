<!-- start of README -->
<h1>JupyterPilot</h1>

<p>Jupyter Pilot is a Python package that uses the OpenAI API to generate code from natural language prompts. It is designed to simplify the process of writing code and to make programming more accessible to non-programmers.</p>

<h2>Installation</h2>

<p>To install Jupyter Pilot, simply run:</p>

<pre><code>pip install jupyterpilot</code></pre>
<a href = 'https://pypi.org/project/jupyterpilot/1.0.0/'>PyPi Link</a>

<h2>Update 1.0.0</h2>
<p>Please run: <i>pip install --upgrade jupyterpilot</i></p>
<li>Removed issues where people were getting In[ ]: in code.</li>
<li>Code insertion in new cell</li>
<li>All parameters of model can be set using CodetoCell()</li>
<li>Improved accuracy with new default params</li>
</p>

<p><i>Note: Most of these errors are model generated. For this exact reason, the code creates a test.py in the same working directory as that of the notebook. User can read and manually or programmatically remove these errors. </p></i>

<h2>Usage</h2>

<p>To use JupyterPilot, import the <code>pysetup</code> class from the <code>jupyterpilot</code> module:</p>

<pre><code>from jupyterpilot import pysetup</code></pre>

<p>Then, create an instance of <code>CodetoCell</code> with your OpenAI API key:</p>

<pre><code>openai_key = "YOUR_API_KEY"
cc = pysetup.CodetoCell(openai_key)</code></pre>

<p>Call the <code>get_code</code> method with a natural language prompt to generate code:</p>

<pre><code>prompt = "Create a function to get stock data from yahoo finance api"
cc.get_code(prompt)</code></pre>

<p>This will create a file called <code>test1.py</code> with the generated code and import statements, and then load the code into a Jupyter Notebook cell for further use.</p>

<h2>Options</h2>

<p>You can pass options to the <code>CodetoCell</code> constructor to customize its behavior:</p>

<pre><code>cc = pysetup.CodetoCell(
    	openai_key=openai_key,
    	model="code-cushman-001", # Choose a different model (optional)
    	tokens=2048, # Increase the number of tokens (optional)
	tokens=1024 # (optional), 
	temperature=0.1 # (optional),
	top_p=1 # (optional),
	penalty=0, # (optional)
	presence_penalty=0 # (optional)
)</code></pre>

<p>You can choose a different model by setting the <code>model</code> parameter to a different model ID. Other models can be found on the <a href="https://beta.openai.com/docs/engines/code-completion">OpenAI API documentation</a>.</p>

<p>You can increase the number of tokens by setting the <code>tokens</code> parameter to a larger value. The maximum number of tokens supported by the <code>code-cushman-001</code> model is 2048, while the <code>code-davinci-002</code> model supports up to 8000 tokens.</p>

<h2>Authors</h2>
<a href="https://www.github.com/ishu121992">@ishu121992</p>

<h2>License</h2>
<p>JupyterPilot is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>
<!-- end of README -->
