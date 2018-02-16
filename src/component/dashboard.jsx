import React from 'react';
import Product from './product.jsx';
import Categories from './categories.jsx';
import Products from './products.jsx';
import product from './product.jsx';

class DashboardView extends React.Component {

    state = {
        productListActiveClass: 'btn-primary',
        pageSize: 3,
        selectedCategory: undefined,
        selectedPage: 1,
        products: [],
        categories: []
    };

    addProductToCart = (product) => {
        //
    };

    setCategory = (category) => {
        const products = this.state.products.filter((product) => product.category === category);
        this.setState(() => ({products}));
    };

    render() {
        return (
            <div className="panel panel-default row" ng-controller="productListCtrl"  ng-hide="data.error">
                <Categories categories={this.state.categories} setCategory={this.setCategory}/>
                <Products products={this.state.products} addProductToCart={this.addProductToCart} selectedPage={this.state.selectedPage}/>
            </div>
        );
    }

    componentDidMount() {
        const json = "[{\"name\":\"Kayak\",\"description\":\"A boat for one person\",\"category\":\"Watersports\",\"price\":275},{\"name\":\"Life Jacket\",\"description\":\"Protective and fashionable\",\"category\":\"Watersports\",\"price\":48.95},{\"name\":\"Soccer Ball\",\"description\":\"FIFA-approved size and weight\",\"category\":\"Soccer\",\"price\":19.5},{\"name\":\"Corner Flags\",\"description\":\"Give your playing field a professional look\",\"category\":\"Soccer\",\"price\":34.95},{\"name\":\"Stadium\",\"description\":\"Flat-packed 35,000-seat stadium\",\"category\":\"Soccer\",\"price\":795000},{\"name\":\"Thinking Cap\",\"description\":\"Improve your brain efficiency by 75%\",\"category\":\"Chess\",\"price\":16},{\"name\":\"Unsteady Chair\",\"description\":\"Secretly give your opponent a disadvantage\",\"category\":\"Chess\",\"price\":29.95},{\"name\":\"Human Chess Board\",\"description\":\"A fun game for the family\",\"category\":\"Chess\",\"price\":75},{\"name\":\"Sedona DX\",\"description\":\"A bike with an aluminum frame\",\"category\":\"Bicycle\",\"price\":419},{\"name\":\"Test\",\"description\":\"Delete me\",\"category\":\"Other\",\"price\":25}]";
        const products = JSON.parse(json);
        const allCategories = products.map((product) => product.category);
        const categories = [...new Set(allCategories)];
        console.log('categories:', categories);
        this.setState(() => ({products}));
        this.setState(() => ({categories}));
    }

}

export default DashboardView;