import React from 'react';
import Product from './product.jsx';

const Products = (props) => (
    <div className="col-8">
        {
            props.products.map((product, index) => (
                <Product
                    key={product.name}
                    product={product}
                    addToCart={props.addProductToCart}
                />
            ))
        }                    
        <div className="pull-right btn-group">
            <a ng-repeat="page in data.products | filter:categoryFilterFn | pageCount:pageSize"
                ng-click="selectPage($index + 1)" className="btn btn-default"
                ng-class="getPageClass($index + 1)">
                Page: {props.selectedPage}
            </a>
        </div>
    </div>
);

export default Products;