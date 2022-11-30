@extends('layouts.main')


@section('main-section')

<section class="mainBackground">
    <div class="mainBackgroundTop">
        <div class="mainContain">
            <div class="mainContainInner">

                <form class="registerForm" action="{{url('/')}}/registration" method="post">
                    @csrf
                    <h2>Drigo</h2>
                    <div class="formInner">
                        <div class="formInnerBox">


                            <input required type="text" name="name" placeholder="full name" name="" id="" value="{{old('name')}}">
                            <span class="registretionErrorShow" style="color: red;">
                                @error('name')
                                {{$message}}
                                @enderror
                            </span>
                        </div>
                        <div class="formInnerBox">
                            <input type="text" required placeholder="user name" value="{{old('username')}}" name="username" id="">
                            <span class="registretionErrorShow" style="color: red;">

                                @if(Session::get('usernameErrorKey'))
                                {{"username already exist"}}
                                @endif
                                @error('username')
                                {{$message}}
                                @enderror
                            </span>
                        </div>
                    </div>
                    <div class="formInner">
                        <div class="formInnerBox">
                            <select required name="category" id="category" name="category" value="{{old('category')}}">
                                <option selected value="Cafe">Cafe</option>
                                <option value="Book Store">Book Store</option>
                                <option value="Hotel">Hotel</option>
                                <option value="Grocery">Grocery</option>
                                <option value="Electronic Device">Electronic Device</option>
                                <option value="Baby Food">Baby Food</option>
                                <option value="Medicine">Medicine</option>
                                <option value="Laundry Store">Laundry Store</option>
                                <option value="Computer shop">Computer shop</option>
                                <option value="Resturent">Resturent</option>
                                <option value="Bank">Bank</option>


                            </select>
                        </div>
                        <div class="formInnerBox">
                            <input value="{{old('shopname')}}" required type="text" name="shopname" placeholder="Shop Name" name="" id="">
                            <span class="registretionErrorShow" style="color: red;">
                                @error('shopname')
                                {{$message}}
                                @enderror
                            </span>
                        </div>
                    </div>

                    <div class="formInner">
                        <div class="formInnerBox">
                            <input value="{{old('latitude')}}" required type="number" name="latitude" placeholder="latitude" name="" id="">
                            <span class="registretionErrorShow" style="color: red;">
                                @error('latitude')
                                {{$message}}
                                @enderror
                            </span>
                        </div>
                        <div class="formInnerBox">
                            <input value="{{old('longitude')}}" required type="number" name="longitude" placeholder="longitude" name="" id="">
                            <span class="registretionErrorShow" style="color: red;">
                                @error('longitude')
                                {{$message}}
                                @enderror
                            </span>
                        </div>
                    </div>

                    <div class="formInner">
                        <div class="formInnerBox">
                            <input value="{{old('email')}}" required type="email" name="email" placeholder="email" name="" id="">
                            <span class="registretionErrorShow" style="color: red;">



                                @if(Session::get('emailErrorKey'))
                                {{"email already exist"}}
                                @endif


                                @error('email')
                                {{$message}}
                                @enderror
                            </span>
                        </div>
                        <div class="formInnerBox">
                            <input required type="password" name="password" placeholder="password" name="password" id="">
                            <span class="registretionErrorShow" style="color: red;">
                                @error('password')
                                {{$message}}
                                @enderror
                            </span>
                        </div>
                    </div>

                    <div class="formInner">
                        <div class="formInnerBox">
                            <input required type="password" name="password_confirmation" placeholder="confirm password" name="" id="">
                            <span class="registretionErrorShow" style="color: red;">
                                @error('confirm_password')
                                {{$message}}
                                @enderror
                            </span>
                        </div>
                    </div>
                    <div class="formInner">
                        <!-- 
                        <input class="registerBtn" type="button" value="SignUp"> -->
                        <button class="registerBtn">SignUp</button>
                    </div>

                </form>
                <div class="registerBottomText">
                    <div class="registerBottomTextInner">
                        <p>If you have no account then you can be <a href="{{url('login')}}">Login</a></p>
                    </div>

                    <!-- 
                    <pre>
 @php
 print_r($errors->all());
 @endphp -->
                </div>
            </div>
        </div>
    </div>
    <div class="mainBackgroundBottom">
        <div class="backgroundImg">
            <img src="{{url('font_end_code/image/logo.png')}}" alt="">
            <img src="{{url('font_end_code/image/logo.png')}}" alt="">

        </div>

    </div>
</section>
@endsection