<template>
    <q-page class="row justify-center">
        <div class="row justify-center items-center fullscreen" id="background-img"></div>
        <div class="row justify-center items-center" id="top-container">
            <div class="justify-center items-center" id="search-box">
                <button id="search-btn"></button>
                <input type="text" placeholder="기분좋다" id="search-text" />
            </div>
        </div>
        <div id="main-container">
            <div class="event-section justify-center items-center">
                <dt class="info">진행중인 이벤트</dt>
                <span class="divider" />
                <src class="img" />
                <dt class="title" style="text-align: center">갈리나의 도마도 축제</dt>
                <dt class="date" style="text-align: center">2024.01.18 ~ 2024.02.21</dt>
            </div>
            <div class="notice-section">
                <dt class="info">공지사항</dt>
                <span class="divider" />
                <li class="contents-li">
                    <dt>1</dt>
                    <dt>2</dt>
                    <dt>3</dt>
                </li>
            </div>
            <div class="maintenance-section">
                <dt class="info">점검</dt>
                <span class="divider" />
                <li class="contents-li">
                    <dt>1</dt>
                    <dt>2</dt>
                    <dt>3</dt>
                </li>
            </div>
        </div>
    </q-page>
</template>
<script>
const baseUrl = 'https://open.api.nexon.com/'
export default {}
</script>
<style src="../../css/test.css"></style>
