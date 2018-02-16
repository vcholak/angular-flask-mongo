import React from 'react';

const Product = (props) => (
    <div className="well" ng-repeat="item in data.products | filter:categoryFilterFn | range:selectedPage:pageSize">
        <h3>
            <strong>{props.product.name}</strong>
            <span className="pull-right label label-primary">
                ${props.product.price}
            </span>
        </h3>
        <button onClick={props.addToCart(props.product)}  className="btn btn-success pull-right">
            Add to Cart
        </button>
        <span className="lead">{props.product.description}</span>
    </div>
);

export default Product;