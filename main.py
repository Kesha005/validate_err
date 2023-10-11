import typer


from app.handler.contact import ContactHandler
from app.db.db import recreate_base



cli_app = typer.Typer()



@cli_app.command()
def migrate():
    recreate_base()
    



@cli_app.command()
def hi():
    print(f'Hi it is a email sender app')


@cli_app.command()
def contacts():
    all_contacts = ContactHandler.get_contacts()
    print(f'ID\t Name\t\t Email\n')
    print(f'-----------------------------------------------------')
    for contact in all_contacts:
        print(f'{contact.id}\t{contact.name}\t\t {contact.email}\n')
        print(f'-----------------------------------------------------')
        
        
@cli_app.command()
def create_contact(name:str, email:str):
    new_contact = ContactHandler.create_new_contact(name, email)
    print(f'New contact succcessfully created')


@cli_app.command()
def show(id:int):
    contact = ContactHandler.get_contact_by_id(id)
    print(f'ID\t Name\t\t Email\n')
    print(f'-----------------------------------------------------')
    print(f'{contact.id}\t{contact.name}\t\t {contact.email}\n')


@cli_app.command()
def update(id:int, name:str='null', email:str='null'):
    if ContactHandler.update_contact(id,name, email) == True:
        print("Contact updated successfully")
    else:
        print("There are some problems on updating")
    
@cli_app.command()
def delete(id:int):
    if ContactHandler.destroy_contact(id) == True:
        print("Contact successfully destroyed")
    else:
        print("There is some problems on destroying")


if __name__ == "__main__":
    cli_app()
    