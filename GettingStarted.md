# Software
- Download and install Archi : https://www.archimatetool.com/download/
- Download coArchi from : https://www.archimatetool.com/plugins/
- Install the plugin : Help -> Manage plugins -> Install -> choose coArchi_0.9.4.archiplugin -> restart Archi.

![Archi plugin modal](images/GS-01-Archi-Plugins.png)

## From the Collaboration menu : 
- Toggle Collaboration Workspace
- Import Remote Model to Workspace

![Archi import remote model](images/GS-02-Import-remote-model.png)

- When no local password is set, set a password to protect your repository on the local machine
- A github token can be obtained here : https://github.com/settings/tokens. Create a classis token and save the token in a safe environment.

![Github personal access token](images/GS-00-Github-PAT.png)

- The "Add Remote Model" popup is shown. 

	Choose :
	```
	URL : https://github.com/statistiekcbs/UNECE-SAF
	User Name : [your github user]
	Password : [Personal access token] 
	```
	Check the Store user name and password checkbox.

![Github personal access token](images/GS-03-Add-remote-model.png)

- The Statistical Architecture Framework [main] should be shown in the Collaboration Workspace part of Archi.
- Right click to open the model.

![Github personal access token](images/GS-04-Open-model.png)


## Collaboration

![Archi collaboration](images/GS-05-Collaboration-modelling.png)

You are now set up to collaborate. Changes to the Model can be published as follows:
- Save the Model (will be asked when necessary)
- Publish Changes
- A commit form will be shown. Give comment on what the commit is.

![Archi commit](images/GS-06-Commit.png)

- Publish.
- Check the repository online if changes are available

![Github published](images/GS-07-Published.png)
