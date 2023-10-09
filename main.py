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
    print(f'Name\t\t Email\n')
    print(f'--------------------------')
    for contact in all_contacts:
        print(f'{contact.name}\t\t {contact.email}\n')
        print(f'----------------------------------')
        
@cli_app.command()
def create_contact(name:str, email:str):
    new_contact = ContactHandler.create_new_contact(name, email)
    print(f'New contact succcessfully created')


#

if __name__ == "__main__":
    cli_app()