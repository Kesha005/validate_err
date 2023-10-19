<?php

namespace App\Http\Controllers;

use App\Models\Contact;
use Illuminate\Http\Request;
use PSpell\Config;

class ContactCrudControl extends Controller
{
  
    public function index()
    {
        $contact = Contact::all();
        return $contact;
    }

   
    public function create()
    {
        //
    }

  
    public function store(Request $request)
    {
        $contact = new Contact($request);
        $contact->store();
    }

   
    public function show($id)
    {
        $contact = Contact::where('id', $id)->first();
    }

  
    public function edit($id)
    {
        $contact = Contact::get_contact($id);
        return $contact;
    }

  
    public function update(Request $request, $id)
    {
        $contact = Contact::get_contact($id);
        $contact_update = Contact::update_contact($contact, $request);
    }

   
    public function destroy($id)
    {
        $contact = Contact::delete_contact($id);
    }
}
