import { connectedRouterRedirect } from 'redux-auth-wrapper/history3/redirect'
import { routerActions } from 'react-router-redux'

export const userIsAduthenticated = connectedRouterRedirect({
  redirectPath: '/login',
  allowRedirectBack: false,
  authenticatedSelector: state => state,
  predicate: state => state.token,
  redirectAction: routerActions.replace,
});