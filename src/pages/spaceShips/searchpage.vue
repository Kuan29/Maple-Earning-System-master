<template>
    <q-page class="row justify-center">
        <div id="background-img"></div>
        <div class="container row justify-center">
            <div class="char-img-container">
                <img src="../../unit/img/char_img.svg" />
                <dt class="char-img-namebox">호두맛먹태깡</dt>
            </div>
            <div class="char-base-container row justify-center">
                <div class="char-base-wrap row justify-center">
                    <dt class="char-base-lv">Lv.270</dt>
                    <div class="char-base-box">
                        <span style="float: right; width: 100%; text-align: center">
                            <dt class="char-base-tag">월드</dt>
                            <dt class="char-base-text">제니스</dt>
                        </span>
                    </div>
                    <div class="char-base-box">
                        <span style="float: right; width: 100%; text-align: center">
                            <dt class="char-base-tag">길드</dt>
                            <dt class="char-base-text">수타</dt>
                        </span>
                    </div>
                    <div class="char-base-box">
                        <span style="float: right; width: 100%; text-align: center">
                            <dt class="char-base-tag">직업</dt>
                            <dt class="char-base-text">미하일</dt>
                        </span>
                    </div>
                    <div class="char-base-box">
                        <span style="float: right; width: 100%; text-align: center">
                            <dt class="char-base-tag">유니온</dt>
                            <dt class="char-base-text">4021</dt>
                        </span>
                    </div>
                    <div class="char-base-box">
                        <span style="float: right; width: 100%; text-align: center">
                            <dt class="char-base-tag">무릉도장</dt>
                            <dt class="char-base-text">49층</dt>
                        </span>
                    </div>
                    <div class="char-base-box">
                        <span style="float: right; width: 100%; text-align: center">
                            <dt class="char-base-tag">인기도</dt>
                            <dt class="char-base-text">11</dt>
                        </span>
                    </div>
                </div>
                <div class="char-base-wrap row justify-center">
                    <div class="char-detail-exp">test</div>
                    <div class="char-propensity-box">
                        <apexchart type="radar" :options="chartOptions" :series="chartSeries" height="150%" width="100%" style="margin-right: 0px" />
                    </div>
                </div>
            </div>
            <div class="main-container"></div>
        </div>
        <!-- <img id="char-img" src="../../unit/img/char_img.svg" />
        <div class="" id="char-namebox">
            <p class="char-name">호두맛먹태깡</p>
        </div>
        <div id="user-info-comm"></div> -->
    </q-page>
</template>
<script>
import VueApexCharts from 'vue3-apexcharts'
export default {
    name: 'TestPage',
    components: {
        apexchart: VueApexCharts
    },
    data() {
        return {
            param_name: '',
            userbasic: {},
            chartOptions: {
                chart: {
                    toolbar: {
                        show: false
                    }
                },
                plotOptions: {
                    radar: {
                        polygons: {
                            strokeColors: '#808080',
                            fill: {
                                colors: ['#C1C1C1']
                            }
                        }
                    }
                },
                colors: ['#5C637D'],
                xaxis: {
                    categories: ['카리스마', '감성', '통찰력', '의지', ' 손재주', '매력']
                },
                yaxis: {
                    max: 100,
                    min: 0
                }
            },
            chartSeries: [
                {
                    data: [80, 22, 81, 27, 66, 44]
                }
            ]
        }
    },
    mounted() {},
    methods: {
        getParams() {
            const currentUrl = window.location.href
            const paramsUrl = new URL(currentUrl)
            paramsUrl.port = 8000
            paramsUrl.href
            fetch(paramsUrl.href)
                .then(res => res.json())
                .then(t => {
                    this.param_name = t
                })
        }
    }
}
</script>
<style src="../../css/user_t.css"></style>
