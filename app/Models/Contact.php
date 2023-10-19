<?php

namespace App\Models;

use Exception;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Contact extends Model
{
    use HasFactory;

    protected $fillable = ['name', 'email', 'job'];

    public function __construct($data)
    {
        $this->name = $this->name;
        $this->email = $this->email;
        $this->job = $this->job;
    }

    public  function store(){
        try {

            $this->create([
            'name'=>$this->name,
            'email'=>$this->email,
            'job'=>$this->job
            
        ]);
        } catch(Exception $e){
            return $e;
        }
        
    }


    public static function get_contact($id){
        $contact = self::where('id', $id)->first();
        return $contact;
    }

    public static function update_contact($contact, $data){
        $contact->update([
            'name' => $data->name,
            'email' => $data->email,
            'job' => $data->job
        ]);
    }

    public static function delete_contact($id){
        try{
        
            self::where('id', $id)->delete();
        } catch(Exception $e){
            return $e;
        }

    }
}
