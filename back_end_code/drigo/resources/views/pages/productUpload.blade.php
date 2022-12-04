@extends('layouts.main');


@section('main-section')
<section class="productUpload">

    <div class="productClose">
        <a href="{{url('sellerProfile')}}" class="closeDiv">
            <i class="gg-close 2x"></i>
        </a>
    </div>

    <div class="productUploadInner">

        <h2 class="uploadTitle"> 
        AddProduct
        </h2>
        <form class="uploadForm" method="post" enctype="multipart/form-data" action="{{url('/')}}/addproduct">
            @csrf
            <div class="formInnerDiv">
                <input type="text" class="productNameField" placeholder="Product Name" value="{{old('product_name')}}" name="product_name" id="">
                <p class="UploadPageError"> @error('product_name')
                    {{$message}}
                    @enderror
                </p>
            </div>
            <div class="formInnerDiv">
                <div class="productInenrDivSize">
                    <input type="number" value="{{old('product_size')}}" class="productSizeField" placeholder="Product Size" name="product_size" id="">

                    <select name="product_size_constans" class="ProductSizeConstans">
                        <option>kg</option>
                        <option>g</option>
                        <option>liter</option>
                        <option>ml</option>
                        <option>unit</option>
                        <option>piece</option>
                    </select>




                </div>
                <p class="UploadPageError"> @error('product_size')
                    {{$message}}
                    @enderror
                </p>
            </div>
            <div class="formInnerDiv">
                <div class="productInenrTextArea">
                    <textarea name="product_details" class="UploadInnerTextArea"></textarea>
                </div>
                <p class="UploadPageError"> @error('product_details')
                    {{$message}}
                    @enderror
                </p>
            </div>
            <div class="formInnerDivPrice">
                <input type="number" value="{{old('price')}}" class="productNameField" placeholder="Price" name="price" id="">
                <p class="UploadPageError"> @error('price')
                    {{$message}}
                    @enderror
                </p>
            </div>
            <div class="fileUpload">
                <input type="file" id="avatar" name="image" accept="image/png, image/jpeg">
                <p class="UploadPageError"> @error('image')
                    {{$message}}
                    @enderror
                </p>
            </div>
            <button class="UploadBtn">Submit</button>
        </form>
    </div>
</section>
@endsection