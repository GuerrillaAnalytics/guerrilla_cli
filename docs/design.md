project
    init: name, location
        * check name is valid, if not exit
        * check location exists, if not exit
        * check folder (name and location) does not already exist
            * if exists with no config file, warn user and ask if they want to continue
            * if exists with a config file, warn user and ask if they want to continue and overwrite file
            * if doesn't exist, create folder 
        * create config file if doesn't exist
        * create pm subfolders
        * create wp subfolders
        * ask for inputs location on file share
        
    config 
        s3
            * ask for inputs location on S3 bucket
            * check for aws config folder?
        postgres?
            
        
    audit: project_location
        * check project folder has correct name
        * check pm folder has right structure
        * check wp folder has right structure
wp
    create: name
        * check location doesn't already exist
    audit
    
build
    init
    audit
    run
    
    
