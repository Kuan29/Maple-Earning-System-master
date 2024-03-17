<template>
    <q-layout view="lHh Lpr lFf">
        <q-header elevated>
            <q-toolbar>
                <q-btn flat dense round icon="menu" aria-label="Menu" @click="toggleLeftDrawer" />

                <q-toolbar-title> MES </q-toolbar-title>
            </q-toolbar>
        </q-header>

        <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
            <q-list>
                <q-item-label header> Links </q-item-label>

                <EssentialLink v-for="link in essentialLinks" :key="link.title" v-bind="link" />
            </q-list>
        </q-drawer>

        <q-page-container>
            <router-view />
        </q-page-container>
    </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue'

export default {
    name: 'MainLayout',

    components: {
        EssentialLink
    },
    data() {
        return {
            leftDrawerOpen: false
        }
    },
    beforeCreate() {
        this.essentialLinks = [
            {
                title: 'Home',
                caption: '',
                icon: 'home',
                link: '/'
            },
            {
                title: 'Test Page - 01',
                caption: 'Nexon API 테스트',
                icon: 'school',
                link: '/test'
            }
        ]
    },
    methods: {
        toggleLeftDrawer() {
            this.leftDrawerOpen = !this.leftDrawerOpen
        }
    }
}
</script>
