mysql -u root -p (logs into )
ALTER USER 'root'@'localhost' IDENTIFIED BY 'rootroot';
FLUSH PRIVILEGES;
quit


## Front end
    template
        list.html (list all recipes)
            {% for recipe in recipes%}
            {{recipe.title}}
            {% endfor %}
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

            change
            change_ingredients
            change_title
            change_description
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