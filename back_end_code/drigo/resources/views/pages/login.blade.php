@extends('layouts.main')


@section('main-section')

<section class="loginMain">
    <div class="loginMainTop">
        <img src="{{url('font_end_code/image/logo.png')}}" alt="">
        <div class="mainItem">
            <div class="mainItemInner">
                <h2>Drigo</h2>
                <form class="mainItemForm" action="{{url('/')}}/login" method="POST">
                    @csrf
                    <div class="inputfield">
                        <input name="username" placeholder="username"   value="{{old('username')}}" type="text">
                        <div class="loginErrorBox">
                            <span style="color: red; font-size:1rem;">

                                @error('username')
                                {{$message}}
                                @enderror
                            </span>
                        </div>
                        <input name="password" placeholder="password" type="password">

                        <div class="loginErrorBox">
                            <span style="color: red; font-size:20px;">

                                @error('password')
                                {{$message}}
                                @enderror
                            </span>
                        </div>
                    </div>
                    <button class="loginBtn">Login</button>
                    <!-- <input class="loginBtn" type="button" value="Login"> -->
                </form>
            </div>
        </div>

    </div>
    <div class="loginMainBottom">
        <img src="{{url('font_end_code/image/logo.png')}}" alt="">
        <div class="loginBottomText">
            <div class="loginBottomTextInner">
                <p>If you have no account then you can be <a href="{{url('registration')}}">SignUP</a></p>
            </div>
        </div>
    </div>
</section>
@endsection