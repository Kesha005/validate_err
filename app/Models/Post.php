<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Post extends Model
{
    use HasFactory;

    protected $fillable = ['name', 'theme', 'body'];

    public function get_all(){
        
    }

    public function show(){

    }

    public function store(){

    }
}
