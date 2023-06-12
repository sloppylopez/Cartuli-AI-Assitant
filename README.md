<!DOCTYPE html>
<html>
<body>
<div style="text-align: center;">
    <img src="https://github.com/sloppylopez/Cartuli-AI-Assitant/blob/main/videos/first_feature.gif" alt="Cartuli AI Assistant" style="max-width: 100%; height: auto;">
</div>



  <h1>Hi!, my name is <strong>Cartuli</strong>.</h1>
 <h2>I'm an 'achsually' useful AI Assistant. Watch me refactoring code automagically.</h2>

<div style="text-align: center;">
    <img src="https://raw.githubusercontent.com/sloppylopez/Cartuli-AI-Assitant/main/videos/Learn_to_Refactor.gif" alt="Cartuli AI Assistant Refactoring code" style="max-width: 100%; height: auto;">
</div>

<h3>Streamlined Voice Commands with Elgato Stream Deck</h3>
<p>With <strong>Cartuli</strong>, you can now give voice commands directly by pressing buttons on your Elgato Stream
    Deck or
    keyboard. Say goodbye to manual input and effortlessly execute actions with a single press. <strong>Cartuli</strong>
    puts the power of automation at your fingertips.</p>

<h3>Web Browsing and Online Searches, ChatGPT</h3>
<p>Need to quickly look up something online? <strong>Cartuli</strong> has got you covered. Open your favorite browser
    with just a command and make online searches without interrupting your workflow. <strong>Cartuli</strong> seamlessly
    integrates with your web browsing experience.This goes without saying but you can also ask questions
    to ChatGPT just using your voice through <strong>Cartuli</strong></p>

<h3>Intellij Idea Integration</h3>
<p><strong>Cartuli</strong> integrates with Intellij Idea, the powerful IDE. But here's the kicker: you can control
    <strong>Cartuli</strong> with your own voice! No more clicking or typing—just speak up, and <strong>Cartuli</strong>
    will be at your service. Need to run tests? Just say it. Want to execute actions? Voice it out. Interacting with
    your project is as easy as having a conversation. Finally, you can code with your feet on your desk, while <strong>Cartuli</strong>
    takes care of the rest. <strong>Cartuli</strong> and Intellij Idea: a perfect match for a hands-free coding
    adventure!</p>

<h3>Configurable Windows Notifications</h3>
<p>Stay informed and up-to-date with <strong>Cartuli</strong>'s configurable Windows notifications. Receive feedback,
    updates, and reminders right on your desktop. Customize your notifications to suit your preferences and never miss
    an important event. Don't forget the floating memes!</p>

<h3>Real Resource Utilization</h3>
<p>Unlike other AI assistants, such as Cortana, Google Assistant, Siri, or JARVIS, <strong>Cartuli</strong> is designed
    to utilize your machine resources. It works harmoniously with your system, allowing you to focus on your tasks
    without any slowdowns or disruptions.</p>

        🤷‍♂️User: Cortana, open youtube, play some rap!
        🤖CORTANA: Say what, say what?
        🤓CARTULI: Yes, my liege

<h3>On-the-fly Configurable Personalities</h3>
<p><strong>Cartuli</strong> isn't just any AI assistant, it's a shape-shifter of personalities! Want
    <strong>Cartuli</strong> to channel the spirit of Donald Trump, delivering answers that are "tremendous" and
    "unbelievable"? No problem! Craving Elvish or Shakespearean responses? Consider it done, thou artless tardy-gaited
    scut!</p>

<h2>Getting Started</h2>

<ol>
    <li>Install the latest version of Windows 11 on your machine.</li>
    <li>Set up your Elgato Stream Deck and ensure it is connected to your system (OPTIONAL).</li>
    <li>Clone the <strong>Cartuli</strong> repository to your local machine.</li>
    <li>Install the required Python packages by running <code>pip install -r requirements.txt</code> (YOU WILL HAVE TO
        INSTALL THEM MANUALLY).
    </li>
    <li>Configure your Elgato Stream Deck with the desired commands and actions.</li>
    <li>Run the <strong>Cartuli</strong> script and enjoy the power of real automation!</li>
</ol>

<section>
    <h2>Dissection</h2>
    <p>In the development of <strong>Cartuli</strong>, we have carefully chosen the tools and libraries that power its
        functionality. Let's take a closer look at the architectural components:</p>

<h3>👂Ears: Python SpeechRecognition</h3>
<p>For speech recognition capabilities, we rely on the powerful Python library called SpeechRecognition. It's a
    versatile and reliable tool that allows <strong>Cartuli</strong> to listen and understand your voice commands
    surprisingly well. With SpeechRecognition, <strong>Cartuli</strong> can accurately capture your instructions and
    initiate the corresponding actions.</p>

<h3>🧠Brain: Spacy for Text Classification</h3>
<p>Spacy is our go-to library for text recognition and understanding. With its advanced natural language processing
    capabilities, <strong>Cartuli</strong>'s brain can analyze and comprehend your commands and queries. Spacy
    enables <strong>Cartuli</strong> to extract meaningful information from the text, empowering it to perform the
    right actions based on your input.</p>

<h3>👄Mouth: Plyer for Windows Notifications</h3>
<p>To provide you with timely feedback and updates, <strong>Cartuli</strong> utilizes the Plyer library for
    displaying Windows notifications. Plyer allows <strong>Cartuli</strong> to deliver important information,
    reminders, and notifications right on your desktop. Whether it's completion notifications, task updates, or
    simply a friendly message, <strong>Cartuli</strong>'s mouth ensures that you stay informed and connected.</p>

<h3>👌Hands: Pygetwindow for Windows Control</h3>
<p>For seamless control over Windows applications, we rely on the Pygetwindow library. Pygetwindow enables <strong>Cartuli</strong>
    to interact with and manipulate windows, allowing it to open programs, switch between applications, and perform
    various window-related tasks. With Pygetwindow, <strong>Cartuli</strong> takes full command of your Windows 11
    environment, making your development experience even smoother.</p>

<p>By leveraging the capabilities of these powerful libraries, <strong>Cartuli</strong> achieves a robust and
    efficient architecture that enables seamless interaction, understanding, and communication. Together, they form
    the foundation of <strong>Cartuli</strong>'s intelligence and assistive capabilities, making it a reliable and
    enjoyable AI Assistant for your Windows 11 environment.</p>
</section>

<section>
    <h2>Voice Commands</h2>
    <p><strong>Cartuli</strong> is designed to understand and execute a set of commands to perform various actions. Here
        are some of the commands that <strong>Cartuli</strong> is intended to support:</p>

<ul>
    <li><strong>open</strong>: Open a specific program or application.</li>
    <li><strong>type</strong>: Simulate typing characters or text.</li>
    <li><strong>search</strong>: Perform a search operation in the terminal.</li>
    <li><strong>play</strong>: Open the music player application.</li>
    <li><strong>run</strong>: Execute a specific script or program.</li>
    <li><strong>chatGPT</strong>: Initiate a conversation with ChatGPT, the powerful language model.</li>
</ul>

<p>By utilizing this set of commands, <strong>Cartuli</strong> provides a user-friendly and efficient interface for
    executing various tasks and automating daily development chores. With just a simply voice <strong>keyword</strong> command,
    <strong>Cartuli</strong> will swiftly carry out your instructions, making your coding experience more enjoyable
    and productive.</p>
</section>


<h2>Contributing</h2>

<p>We welcome contributions from the community to make <strong>Cartuli</strong> even better. If you have any ideas, bug
    fixes, or feature suggestions, please submit a pull request or open an issue on our GitHub repository.</p>

<h2>License</h2>

<p><strong>Cartuli</strong> is released under the <a href="LICENSE">MIT License</a>.</p>

<h2>Acknowledgements</h2>

<p>We would like to express our gratitude to the open-source community for their valuable contributions and support in
    making <strong>Cartuli</strong> a reality.</p>

<p>Join us on this exciting journey with <strong>Cartuli</strong>, your actually helpful AI Assistant for Windows 11.
    Let's automate and streamline our daily development chores like never before! 🚀🤖🤓</p>

<h2>Disclaimer</h2>

<h3><strong>Cartuli</strong> - AI Assistant</h3>

<p>Please note that <strong>Cartuli</strong> is a work in progress and may contain bugs or errors. The code and
    accompanying files provided in this repository are for informational and educational purposes only. We, the creators
    of <strong>Cartuli</strong>, cannot guarantee the accuracy, reliability, or effectiveness of the code and disclaim
    any responsibility for any damage, loss, or negative impact that may arise from the use of this code.</p>

<p>Using <strong>Cartuli</strong> or any part of its codebase is at your own risk. We strongly recommend reviewing and
    testing the code thoroughly before using it in any critical or production environment. Additionally, exercise
    caution and ensure you have appropriate backups and safeguards in place to prevent any unintended consequences or
    data loss.</p>

<p>Please be aware that as <strong>Cartuli</strong> is continuously being developed and improved, the code and
    functionalities may change over time. We encourage contributions, suggestions, and bug reports from the community to
    help make <strong>Cartuli</strong> more robust and reliable.</p>

<p>Remember to use <strong>Cartuli</strong> responsibly and comply with all applicable laws and regulations. We disclaim
    any liability for any misuse, unethical or illegal activities carried out using <strong>Cartuli</strong>.</p>

<p>Thank you for your understanding and collaboration in making <strong>Cartuli</strong> a better AI assistant.</p>
<section>
    <h2>I Want You!</h2>
    <h3>Join Us in Developing <strong>Cartuli</strong> - The Actually Helpful AI Assistant</h3>
    <div style="text-align: center;">
        <img src="images/uncle-sam-cartuli.jpg" alt="Uncle Sam" width="300" height="300">
    </div>
    <p>We are on a mission to create the best AI Assistant in the world, and we need your help to make it happen! At
        <strong>Cartuli</strong>, we believe in empowering developers to code from the bed, the couch, or wherever they
        desire, with the most incredible AI Assistant ever created.</p>
    <p>We are looking for talented and enthusiastic developers to join our ranks and contribute to the development of
        <strong>Cartuli</strong>. With your expertise and passion, we can make <strong>Cartuli</strong> shamelessly
        better than Cortana, Siri, Google Assistant, and even Microsoft Jarvis!</p>
    <p>Imagine a world where developers have a powerful and intuitive AI Assistant that understands their needs,
        executes tasks flawlessly, and brings joy to their coding experience. Together, we can revolutionize the way
        developers work and bring <strong>Cartuli</strong> to every coder's workstation.</p>
    <p>If you are ready to embark on this exciting journey and be a part of the <strong>Cartuli</strong> revolution,
        join our team of dedicated developers. Let's create the AI Assistant that will make coding dreams come true, so
        developers can code from the bed finally!</p>
    <p>Are you up for the challenge? Join us now!</p>
</section>

<section>
    <h2>Current State of Affairs</h2>
  <p>Cartuli AI Assistant is here, ready to make your life easier and more productive than ever before!</p>

  <h3>Feature 1: Seamless Windows 11 Terminal Integration</h3>
  <p>With Cartuli AI Assistant, you can now unleash the power of your Windows 11 default terminal with just the press of a button!</p>

  <p>Simply press the number a key on your keyboard/elgato Stream Deck, and Cartuli will eagerly be listening to your commands.</p>

  <p>Don't worry if you're not sure what to say! or if he does not understand you, after few seconds you will be able to enter the command manually.</p>

  <p>And that's just the beginning! We have many more exciting features in the pipeline, designed to revolutionize your digital experience.</p>

  <p>Stay tuned for future updates as we continue to enhance Cartuli AI Assistant, making it your ultimate digital companion for productivity, entertainment, and so much more!</p>

</section>
<section>
    <h2>Interest Links</h2>
    <p>https://platform.openai.com/docs/api-reference/completions/create</p>
    <p>https://www.youtube.com/watch?v=dIUTsFT2MeQ</p>
    <p>https://www.youtube.com/watch?v=Qos2rG3zVAM</p>
    <p>https://openai.com/pricing#language-models</p>
</section>
<h2>Setting up the <code>OPENAI_API_KEY</code> environment variable</h2>

<p>To use this project, you'll need to set up an environment variable called <code>OPENAI_API_KEY</code>. This is a secret API key provided by OpenAI that's required to access their APIs.</p>

<p>Here's how you can obtain your <code>OPENAI_API_KEY</code>:</p>

<ol>
  <li>Visit the <a href="https://beta.openai.com/docs/api-reference/introduction">OpenAI API website</a>.</li>
  <li>Click on the "Sign up for OpenAI" button and follow the instructions to create an account.</li>
  <li>Once you have created an account, log in to the OpenAI API website.</li>
  <li>Navigate to the "API keys" section of your account dashboard.</li>
  <li>Click on the "Generate new key" button to create a new API key.</li>
  <li>Copy the generated API key.</li>
  <li>Set the <code>OPENAI_API_KEY</code> environment variable in your local environment by running the following command in your terminal (replacing <code>&lt;YOUR_API_KEY&gt;</code> with your actual API key):</li>
</ol>

<pre><code>export OPENAI_API_KEY=&lt;YOUR_API_KEY&gt;</code></pre>

<p>Alternatively, you can also set the <code>OPENAI_API_KEY</code> environment variable in a configuration file such as <code>.env</code>, which can be loaded by your project's code.</p>

<p>Once you have set up the <code>OPENAI_API_KEY</code> environment variable, you should be able to use the OpenAI APIs in your project.</p>

<div style="text-align: center;">
    <h2>Powered by</h2>
    <img src="images/Python-logo-notext.svg.png" alt="ChatGPT Logo" width="200" height="200">
    <img src="images/ChatGPT_logo.svg.png" alt="Python Logo" width="200" height="200">
    <img src="images/elgato-logo.png" alt="Elgato Logo" width="200" height="200">
    <img src="images/wsl.png" alt="WSL Logo" width="200" height="200">
</div>

<section>
  <h2>Image Ownership Disclaimer</h2>
  <p>
    The images used in this GitHub repository belong to their respective owners and are used for demonstration purposes only. I, as the creator of the AI bot Assistant named Cartuli, do not claim ownership of these images.
  </p>

<h3>Copyright Notice</h3>
  <p>
    All visual content, including images, logos, and graphics, are the property of their respective owners. These images have been sourced from various publicly available platforms and are used solely for illustrative purposes.
  </p>

  <p>
    If you believe that any copyrighted material has been used without proper permission or attribution, please contact me, and I will promptly address the concern.
  </p>
</section>
</body>
</html>

