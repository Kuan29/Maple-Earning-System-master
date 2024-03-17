Write-Output "Project Initialize Running"

if ( (node -v).length -le 0) {
    throw "node.js를 찾을 수 없습니다."
}
$nodeVer = ((node -v) -split '\.')[0]
if ([int]($nodeVer.substring(1, $nodeVer.length - 1)) -gt 14) {
    npm i
} else {
    throw "node.js 버전이 낮아 초기 세팅을 진행할 수 없습니다. 14버전 이상 사용 가능합니다. 현재 버전: $nodeVer"
}

# mv -Path ".\frontend\.vscode" -Destination ".\"
# ac -Path ".\.vscode\settings.json" -Value '"eslint.workingDirectories": ["./frontend"]'

if ( (python -V).length -gt 0 ) {
    $pythonVer = ((python -V) -split '\.')
    $pyComm = python -m pip install -r requirements.txt
} else {
    $pythonVer = ((py -V) -split '\.')
    $pyComm = py -m pip install -r requirements.txt
}
if ( $pythonVer.length -le 0 ) {
    throw "Python을 찾을 수 없습니다."
}
if ( [int]($pythonVer[0].substring(7, 1)) -ne 3 ) {
    throw "Python 버전이 낮아 진행할 수 없습니다. 3버전 이상 사용 가능합니다. 현재 버전: $pythonVer[0]"
} elseif ( [int]($pythonVer[1]) -gt 11) {
    throw "Python 버전이 낮아 진행할 수 없습니다. 3.11버전 이상 사용 가능합니다. 현재 버전: $pythonVer"
} else {
    $pyComm
}

Write-Output "Project Initialize Done."
