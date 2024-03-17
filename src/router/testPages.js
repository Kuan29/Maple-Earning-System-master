import MainLayout from 'layouts/MainLayout.vue'

export default [
    {
        path: '/test',
        component: () => MainLayout,
        children: [{ path: '', component: () => import('pages/spaceShips/TestPage.vue') }]
    },
    {
        path: '/maintest',
        component: () => MainLayout,
        children: [{ path: '', component: () => import('pages/spaceShips/MainPage_T.vue') }]
    },
    {
        path: '/test/:search',
        component: () => MainLayout,
        children: [{ path: '', component: () => import('pages/spaceShips/searchpage.vue') }]
    }
]
