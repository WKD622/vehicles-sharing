import { combineReducers } from 'redux'

const initialState = {
    token: '',
};

const rootReducer = (state = [], action) => {
    switch (action.type) {
        case 'SET_TOKEN':
            return {
                ...state,
                token: action.token,
            };
        case 'REMOVE_TOKEN':
            return {
                ...state,
                token: '',
            };
        default:
            return state
    }
}

export default rootReducer;
