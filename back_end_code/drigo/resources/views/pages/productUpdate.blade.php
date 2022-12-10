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
            Update Product
        </h2>
        <form class="uploadForm" method="post" enctype="multipart/form-data" action="{{url('/')}}/updateProduct">
            @csrf
            <!-- Here these lower line have no work it only send the product edit id -->
            <select class="product_edit_hide" name="edit_id">
                <option>{{$editProducts->product_id}}</option>
            </select>
            <!-- Here these upper line have no work it only send the product edit id -->

            <div class="formInnerDiv">
                <input type="text" class="productNameField" placeholder="Product Name" value="{{$editProducts->product_name}}" name="product_name" id="">
                <p class="UploadPageError"> @error('product_name')
                    {{$message}}
                    @enderror
                </p>
            </div>
            <div class="formInnerDiv">
                <div class="productInenrDivSize">
                    <input type="number" value="{{
                        
                        $getOnlySizeWithInteger=(int) filter_var($editProducts->product_size,FILTER_SANITIZE_NUMBER_INT)}}" class="productSizeField" placeholder="Product Size" name="product_size" id="">

                    <select name="product_size_constans" class="ProductSizeConstans">
                        <option>kg</option>
                        <option>g</option>
                        <option>liter</option>
                        <option>ml</option>
                        <option>unit</option>
                        
                    </select>




                </div>
                <p class="UploadPageError"> @error('product_size')
                    {{$message}}
                    @enderror
                </p>
            </div>
            <div class="formInnerDiv">
                <div class="productInenrTextArea">
                    <textarea name="product_details" class="UploadInnerTextArea">{{$editProducts->product_details}}</textarea>
                </div>
                <p class="UploadPageError"> @error('product_details')
                    {{$message}}
                    @enderror
                </p>
            </div>
            <div class="formInnerDivPrice">
                <input type="number" value="{{$editProducts->product_price}}" class="productNameField" placeholder="Price" name="price" id="">
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