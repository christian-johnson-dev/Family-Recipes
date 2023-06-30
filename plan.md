Version 2.0
Delete record delete associated picture
Add ingredients table
Commenting to comments
Adding separate families
Data points
    servings
Add tags
    Provided by user
    gluten-free, desert, ....
Recipes API
    get nutritional info
Ability to pair recipes
Prevent accidental creation of data

Update ingredient quantity given serving size




## Front end
        
## Back end
    controllers
        comments
            create (save)
            delete
            edit
            get_recipes_comments
        recipes
        users
    models
        recipe
WORKS       save
WORKS       get_all_recipes
WORKS       validate_recipe
WORKS       get_one_recipe
WORKS       delete


WORKS        change_ingredients
WORKS        change_title
WORKS        change_description
             change_image
        user

        comment
            create (save)
            delete
            edit (change)
            get_all
## Branches of development - frontend, backendcomments, backendrecipes
## Search by partial in MySQL
## Add image
## Comment on comments?
## Ingredients table
## Steps table
## user route/ needs to list of recipes not index.html
## edge case of no recipes Indexerror one_recipe/1

mysql -u root -p (logs into )
ALTER USER 'root'@'localhost' IDENTIFIED BY 'rootroot';
FLUSH PRIVILEGES;
quit
