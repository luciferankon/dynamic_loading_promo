Step 1: Installing Gauge on Windows
-----------------------------------

This section gives specific instructions on setting up Gauge in a Microsoft Windows environment.
You can install Gauge using any of the following methods. We recommend using the Windows installer.

.. tab-container:: Windows-Options

    .. tab:: Windows Installer

        Download the following installation bundle to het the latest stable release of Gauge.

        
    .. tab:: Chocolatey Package Manager

         System Requirements
             Chocolatey Package Manager
        
        For this to work, you will need to install Chocolatey. If you have chocolatey installed then all you need to do is to follow the steps below, it will download and install Gauge.

         Note:
         Some of the following instructions mention the "command prompt". Where this is used, it refers to the Windows cmd.

         - To open your Command prompt, click your Start Button
         - In Search type, "cmd"
         - Then click on "Command Prompt"
         - Type the following command in your Command Prompt to install Gauge.

        .. code-block:: console

           choco install gauge

    .. tab:: Zip File

        1.  Download the following zip installer
        2.  Extract it to a location and add it to your system path using the following command in powershell


        .. code-block:: console

           PS> Expand-Archieve -Path gauge-1.0.5-windows.x86_64.zip -Destination-path custom_path
    .. tab:: Npm Installer

         System Requirements
             Node.js
             To install gauge using NPM you will need the latest node version

              - If you have nodejs already installed - to get the latest version use the following command:
                `npm install -g npm@latest`.
        
        You can install gauge by running the following command in Powershell/Command Prompt

        .. code-block:: console

            npm install -f @getgauge/cli
        
        