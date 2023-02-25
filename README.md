<!-- start of README -->
<h1>JupyterPilot</h1>

<p>JupyterPilot is a Python package that uses the OpenAI API to generate code from natural language prompts. It is designed to simplify the process of writing code and to make programming more accessible to non-programmers.</p>

<h2>Installation</h2>

<p>To install JupyterPilot, simply run:</p>

<pre><code>pip install JupyterPilot</code></pre>

<h2>Usage</h2>

<p>To use JupyterPilot, import the <code>CodetoCell</code> class from the <code>JupyterPilot.api</code> module:</p>

<pre><code>from JupyterPilot.api import CodetoCell</code></pre>

<p>Then, create an instance of <code>CodetoCell</code> with your OpenAI API key:</p>

<pre><code>openai_key = "YOUR_API_KEY"
cc = CodetoCell(openai_key)</code></pre>

<p>Call the <code>get_code</code> method with a natural language prompt to generate code:</p>

<pre><code>prompt = "Create a function to get stock data from yahoo finance api"
cc.get_code(prompt)</code></pre>

<p>This will create a file called <code>test1.py</code> with the generated code and import statements, and then load the code into a Jupyter Notebook cell for further use.</p>

<h2>Options</h2>

<p>You can pass options to the <code>CodetoCell</code> constructor to customize its behavior:</p>

<pre><code>codetocell = CodetoCell(
    openai_key=openai_key,
    model="code-cushman-001", # Choose a different model (optional)
    tokens=2048 # Increase the number of tokens (optional)
)</code></pre>

<p>You can choose a different model by setting the <code>model</code> parameter to a different model ID. Other models can be found on the <a href="https://beta.openai.com/docs/engines/code-completion">OpenAI API documentation</a>.</p>

<p>You can increase the number of tokens by setting the <code>tokens</code> parameter to a larger value. The maximum number of tokens supported by the <code>code-cushman-001</code> model is 2048, while the <code>code-davinci-002</code> model supports up to 8000 tokens.</p>

<h2>License</h2>

<p>JupyterPilot is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>
<!-- end of README -->
