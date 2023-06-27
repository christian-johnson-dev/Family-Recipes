List

one_recipe
    recipe
        change to allow non login user
        hide edit buttons for one recipe
        hide comment submit box and submit button
        click username go to their recipes
    comments
        edit button

Create  




## Front end
    template
        list.html (list all recipes)
        create-recipe.html
            add to form /save_recipe

        recipe.html (display one recipe)

    static
    css
        
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
