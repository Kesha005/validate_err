<?php

use App\Http\Controllers\SendMail;
use Illuminate\Support\Facades\Route;





Route::get('/',[SendMail::class,'mail_page'])->name('home');

Route::post('/send_mail',[SendMail::class,'send_mail'])->name('mail.send');