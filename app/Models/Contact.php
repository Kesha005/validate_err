<?php

namespace App\Models;

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
        $this->create([
            'name'=>$this->name,
            'email'=>$this->email,
            'job'=>$this->job
        ]);
    }

    public static function update_contact($id, $data){
        $contact = self::where('id', $id)->first();
    }
}
