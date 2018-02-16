import React from 'react';
import {Link,NavLink} from 'react-router-dom';

const Category = (props) => {
    const categoryLnk = `/products?category=${props.category}`;
    return (
    <div>
    <Link to='/products' className="btn btn-block btn-default btn-lg">All Products</Link>
    <NavLink to={categoryLnk} activeClassName='is-active'>{props.category}</NavLink>
     <a  ng-repeat="item in data.products | orderBy:'category' | unique:'category'"
                        ng-click="selectCategory(item)" className="btn btn-block btn-default btn-lg"
                        ng-class="getCategoryClass(item)">
                        {props.selectedCategory}
    </a>
    </div>
    );
}

export default Category;
