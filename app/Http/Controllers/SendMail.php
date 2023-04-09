<?php

namespace App\Http\Controllers;

use App\Mail\MailSend;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Mail;

class SendMail extends Controller
{

    public function mail_page()
    {
        return view('mail_page');
    }

    public function send_mail(Request $request)
    {
        $request->validate(['to'=>'required','text'=>'required']);
        Mail::to($request['to'])->send(new MailSend($request));
    }
}
