<template>
    <q-page padding>
        <div>테스트다악</div>
        <div class="row">
            <q-input v-model="charName" label="Standard" />
            <q-btn color="primary" label="getID" @click="getID" />
            <q-btn color="primary" label="getChar" @click="getChar" />
            <q-btn color="primary" label="DB" @click="goToSearch" />
        </div>

        <div class="row" id="logging"></div>
    </q-page>
</template>
<script>
const baseUrl = 'https://open.api.nexon.com/'
export default {
    name: 'TestPage',
    data() {
        return {
            token: 'test_23671a87ae38740c2acb8db1d2d0d42eaac4b69edaf4cdab1a55f1cedf48d2207849f6e18e83a0942823ab3d3e14b22f',
            url: {
                id: baseUrl + 'maplestory/v1/id?character_name=',
                character: baseUrl + '/maplestory/v1/character/basic?ocid='
            },
            ocid: '',
            charName: '',
            docel: null
        }
    },
    mounted() {},
    methods: {
        getID() {
            const urlString = this.url.id + this.charName

            const res = fetch(urlString, {
                headers: {
                    'x-nxopen-api-key': this.token
                }
            })
                .then(response => response.json())
                .then(data => {
                    this.ocid = data.ocid
                    document.getElementById('logging').innerText += data.ocid
                })
                .catch(error => {
                    document.getElementById('logging').innerText += error
                })
        },
        getChar() {
            // moment js
            const urlString = this.url.character + this.ocid + '&date=2024-01-12'

            const res = fetch(urlString, {
                headers: {
                    'x-nxopen-api-key': this.token
                }
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    document.getElementById('logging').innerText += JSON.stringify(data)
                })
                .catch(error => console.error(error))
        },
        getDb() {
            fetch('http://localhost:8000/test', {
                method: 'GET'
            })
                .then(res => res.json())
                .then(d => console.log(d))
        },
        goToSearch() {
            if (this.charName !== '') {
                this.$router.push({ path: '/test/search', query: { character_name: this.charName } })
            }
        }
    }
}
</script>
<style lang="scss" scoped>
.q-page {
    padding: 20px;
    .row {
        word-break: break-all;
    }
}
</style>
