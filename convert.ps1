$directory = "c:\Users\anari\Documents\New folder\knightmobs\TheKnightMobs-Esports"
$htmlFiles = @('contact.html', 'live.html', 'login.html', 'privacy.html', 'shop.html', 'team.html', 'terms.html', 'tournament.html', 'thankyou.html')

foreach ($htmlFile in $htmlFiles) {
    $inputPath = Join-Path $directory $htmlFile
    $outputPath = Join-Path $directory ($htmlFile -replace '\.html', '.php')
    
    if (Test-Path $inputPath) {
        $content = Get-Content $inputPath -Raw -Encoding UTF8
        
        $content = '<?php session_start(); ?>' + "`n" + $content
        $content = $content -replace 'href="([^"]+)\.html"', 'href="$1.php"'
        $content = $content -replace "href='([^']+)\.html'", "href='$1.php'"
        $content = $content -replace '(?s)<header[^>]*>.*?</header>', "<?php include 'includes/navbar.php'; ?>"
        
        Set-Content -Path $outputPath -Value $content -Encoding UTF8 -Force
        Write-Host "Created $(Split-Path $outputPath -Leaf)"
    }
}
