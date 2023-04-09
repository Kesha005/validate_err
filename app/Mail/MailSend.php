<?php

namespace App\Mail;

use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Mail\Mailable;
use Illuminate\Queue\SerializesModels;

class MailSend extends Mailable
{
    use Queueable, SerializesModels;

    protected $mail_data;
  
    public function __construct($mail_data)
    {
        $this->mail_data=$mail_data;
    }

    public function build()
    {
        return $this->mail_data->subject('Test email')->view('email.test');
    }
}
