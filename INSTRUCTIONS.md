# ICC Homeport Workshop Instructions

# Getting Started with Homeport
## Create account on hub.homeport.ai
1. Go to [Homeport](https://hub.homeport.ai/).
2. Click on "New User? Register"
3. Provide information
4. Confirm email address
5. Login

## Create a new workspace
1. Click on "Add"
2. Provide a name for your workspace
3. "Save"
4. Select the workspace

## Create a Data Source
1. Click on "Data Sources" in the left sidebar
2. "Create Folder"
3. Provide a name and a description
4. "Create Folder"

## Create Assistant
1. Click on "Assistants" in the left sidebar
2. "Create Assistant"
3. Provide a name 
4. Select a base model (e.g. Alibaba Qwen 3 VL 235B)
5. "Select Files and Folders"
6. Select the Data Source folder you created earlier
7. "Additional Features" - Enable "Document Management"
8. Click the back button (top left corner on the screen)


# Using the Homeport API
## Setup python environment
1. Install Python 3.10 or higher
2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Open "Homeport API Usage Examples" notebook
4. Create/Set python interpreter for the project (./venv/bin/python)

## Generate API Key
1. Click your profile icon (bottom right corner)
2. "Settings"
3. "Account"
4. "Create new secret key"
5. Copy the key and paste it in "Homeport API Usage Examples" notebook
6. Open the "Homeport API Usage Examples" notebook and follow the instructions