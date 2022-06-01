<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;

class UserController extends Controller
{
    /**
     * Register a new user
     *
     * 
     */
    public function register(Request $request)
    {
        $user = User::where('email', $request['email'])->first();

        if($user){
            $response['status'] = 0;
            $response['message'] = 'Email Already Exists';
            $response['code'] = 409;
            return response()->json($response);
        }

        $user = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => bcrypt($request->password)
        ]);
        $response['status'] = 1;
        $response['message'] = 'User registered successfully';
        $response['code'] = 200;
        return response()->json($response);
    }
}
