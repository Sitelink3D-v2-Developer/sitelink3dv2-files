# Sitelink3D v2 Files Sample
This repository contains sample scripts for both Windows and Linux operating systems which demonstrate a basic interaction with the Sitelink3D v2 API to:
- [make folders](./make-folder/)
- [upload file](./file-upload/)
- [list files](./file-listing/)
- [download file](./file-download/)

Let's get started!

## Step 1. Install Python
An installation of Python is required to run the sample scripts. At time of writing, Python 3.9.1 is the recommended version.

You can download Python 3.9.1 from:
- [Windows](https://www.python.org/downloads/windows/)
- [Linux](https://www.python.org/downloads/source/)

*NOTE: When installing Python, make sure to include it in the system PATH settings*

## Step 2. Install required Python libraries
To install the required Python libraries, open a console in the repository root and;

for Windows users, run:
```
setup.bat
```
or, for Linux users, run:
```
setup.sh
```

## Step 3. Configure new Site
For Windows users, edit the `create-site.bat` file and for Linux users, edit the `create-site.sh` file to provide the following:

The Sitelink3D v2 environment to create the new Site on. The options are either "prod" or "qa".
```
env=""
```

The Data Centre (dc) to create the new Site.
```
dc=""
```

The 64 alpha-numeric ID string of the target Site. This can be found in `the Sitelink3D v2 web portal -> Site menu -> Site Information` menu.
```
siteid=""
```

Your client OAuth details provided by the Sitelink support team.
For more information, please refer to the `Sitelink3D v2 -> Integrating -> Getting Started` documentation on the [Topcon Software Developer Network](https://developer.topcon.com/en/) site.
```bash
oauth_id=""
oauth_secret=""
oauth_scope=""
```

### Step 3.1 Configure Make New Folder
[Make folder settings:](./make-folder/):
```bash
folder_name="New Folder"
folder_uuid=
parent_uuid=
```

### Step 3.2 Configure File Upload
[File Upload setting:](./file-upload/)
```bash
file_uuid=
folder_uuid=
file_path="/file/location.test"
```

### Step 3.3 Configure File Listing
[File Listing settings:](./file-listing/)
```bash
limit="20"
# start id uuid
start=
```

### Step 3.4 Configure File Download
[File Listing settings example:](./file-download/)
```bash
file_uuid="0f8b8acb-37ce-4dd2-9f2b-fc5f4f476cb4"
```

## Step 4. Run the scripts
To run the scripts, open a console in the corresponded folder name;
- [/make-folder](./make-folder/)
- [/file-upload](./file-upload/)
- [/file-listing](./file-listing/)
- [/file-download](./file-download/)

* for Windows users, run bat file
* for Linux users, run bash script

## Step 5. Inspect the results
You can verify the files Upload/Listing/New folders within the Sitelink3D v2 web portal.
