# copilot

## Testing the copilot in vscode  
### (just purely following)
https://github.com/github/copilot-docs/blob/main/docs/visualstudiocode/gettingstarted.md#getting-started-with-github-copilot-in-visual-studio-code


1. Installing the Visual Studio Code extension
Open vscode and search for `GitHub.copilot` at Menu: View/Extensions


2. Seeing your first suggestion

GitHub Copilot provides suggestions for dozens of languages and a wide variety of frameworks, but it works especially well for Python, JavaScript, TypeScript, Ruby, and Go. The following samples are in JavaScript, but other languages will work similarly.

    Create a new JavaScript (.js) file.

3. Choosing alternate suggestions


* Instead of pressing Tab:
    On Linux, press Alt+] (or Alt+[).

* When you see a suggestion you like, press Tab to accept it.
* If you don't like any of the suggestions, press Esc.


4. Getting more suggestions

Press Ctrl+Enter. GitHub Copilot will open a new tab and suggest multiple options, as shown below.

Suggestions window

Pick a suggestion that you like, then click "Accept Solution" to continue.

If you don't like any of the returned suggestions, just close the suggestions tab.


5. Generating code from a comment

GitHub Copilot can understand significantly more context than most code assistants, and can generate entire functions from something as simple as a comment.

    Create a new JavaScript file, and type the following:

    // find all images without alternate text
    // and give them a red border
    function process() {

6. Using a framework

GitHub Copilot is especially useful for working with APIs and frameworks you're unfamiliar with. Here, we'll use GitHub Copilot to create a simple Express server that returns the current time.

    Create a new JavaScript file, type the following comment, and then press Enter.

    // Express server on port 3000

7. More examples

https://github.com/github/copilot-docs/tree/main/gallery


8. Keyboard shortcuts

The following lists the most common keyboard shortcuts relevant for GitHub Copilot. If you wish to rebind them, check out the configuration guide.

    Accept an inline suggestion: Tab.

    Dismiss an inline suggestion: Esc.

    Show next inline suggestion: Alt + ] or Option + ].

    Show previous inline suggestion: Alt + [ or Option + [.

    Trigger inline suggestion: Alt + \ or Option + \.

    Open Copilot (10 suggestions in separate pane): Ctrl + Enter.


9. Enabling and disabling GitHub Copilot

The GitHub Copilot status icon in the bottom panel of the VSCode window indicates whether GitHub Copilot is enabled or disabled. Its background is blue when enabled, and red when disabled. To enable or disable GitHub Copilot, click the icon. You will be asked whether you wish to toggle for the current file type, or globally.

## errors 

* sorted out
```
[error] ["incompatible: Unable to install 'github.copilot' extension because it is not compatible with the current version of VS Code (version 1.52.1)."," 

```
update vscode 1.61.2
