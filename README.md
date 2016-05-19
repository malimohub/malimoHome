# Malcolm Monroe Portfolio and Website 

This application supports my website/portfolio. It is current and will be constanty updated. The site contains a bit about myself, work experience, and links to my LinkedIn profile, as well as, git hub public repositories I am active in. You can reach the site at http://malimohub.com.

# Dependencies

        - python
        - python-pip
        - supervisor
        - virtualenv

# Getting Started 

Git the project local with the following command:

        $ git clone https://github.com/mmonroe86/malimoHome.git


Include virtual environment in project and activated the environment:

        $ virtualenv malimoHome
        $ source malimoHome/bin/activate

'cd' into the project directory and run the following command to install all project requirements:

        $ pip install -r requirements.txt

Requirements include:

        - Flask
        - requests

Edit line 2 of the starter.sh bash file:

        pushd /path/to/project/directory 

Edit the command value in supervisor.conf file under program malimoHome:

        command = /path/to/bin/./starter.sh

To start the application run:

        $ supervisord

Check if application is running:

        $ supervisorctl 
