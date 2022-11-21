@extends('layouts.main');


@section('main-section')
<section class="productUpload">
    <div class="productUploadInner">
        <h2 class="uploadTitle">Upload Product</h2>
        <form class="uploadForm" action="">
            @csrf
            <div class="formInnerDiv">
                <input type="text" class="productNameField" placeholder="Product Name" name="" id="">
                <p class="UploadPageError"> Invalid Item</p>
            </div>
            <div class="formInnerDiv">
                <div class="productInenrDivSize">
                    <input type="number" class="productSizeField" placeholder="Product Name" name="" id="">

                    <select class="ProductSizeConstans">
                        <option>kg</option>
                        <option>g</option>
                        <option>liter</option>
                        <option>ml</option>
                    </select>




                </div>
                <p class="UploadPageError"> Invalid Item</p>
            </div>
            <div class="formInnerDiv">
                <div class="productInenrTextArea">
                    <textarea class="UploadInnerTextArea"></textarea>
                </div>
                <p class="UploadPageError"> Invalid Item</p>
            </div>
            <div class="formInnerDivPrice">
                <input type="number" class="productNameField" placeholder="Price" name="" id="">
                <p class="UploadPageError"> Invalid Item</p>
            </div>
            <div class="fileUpload">
                <input type="file" id="avatar" name="avatar" accept="image/png, image/jpeg">

            </div>
            <button class="UploadBtn">Submit</button>
        </form>
    </div>
</section>
@endsection