<?php

namespace App\Http\Controllers;

use App\Models\Contact;
use Illuminate\Http\Request;

class ContactCrudControl extends Controller
{
  
    public function index()
    {
        //
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
        
    }

  
    public function edit($id)
    {
        //
    }

  
    public function update(Request $request, $id)
    {
        
        $contact_update = Contact::update_contact($id, $request);
    }

   
    public function destroy($id)
    {
        //
    }
}
