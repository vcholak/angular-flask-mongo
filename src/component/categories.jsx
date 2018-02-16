import React from 'react';
import Category from './category.jsx';

const Categories = (props) => (
    <div className="col-3">
        {
            props.categories.map((category) => (
                <Category category={category} key={category} setCategory={props.setCategory}/>
            ))
        }                    
    </div>
);

export default Categories;