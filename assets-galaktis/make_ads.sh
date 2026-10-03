#!/bin/bash
# Montaż reklam 9:16 z gotowych assetów (bez nowych generacji). Wymaga ffmpeg.
set -e
cd "$(dirname "$0")"
F=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
LOGO=../brand/galaktis-logo-biale.png
T=$(mktemp -d)
COVER="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30,format=yuv420p"

txt() { printf '%s' "$2" > "$T/$1.txt"; }
# hook u góry kadru, biały tekst na półprzezroczystym pasku
hook() { echo "drawtext=fontfile=$F:textfile=$T/$1.txt:fontsize=62:fontcolor=white:line_spacing=14:box=1:boxcolor=black@0.45:boxborderw=28:x=(w-text_w)/2:y=230"; }

vid() { ffmpeg -v error -y -i "$1" -t "$2" -vf "$COVER,$3" -an -c:v libx264 -crf 21 -preset fast "$4"; }
still() { ffmpeg -v error -y -loop 1 -i "$1" -t "$2" -vf "scale=1188:2112,zoompan=z='1+0.0008*on':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d=1:s=1080x1920:fps=30,setsar=1,format=yuv420p,$3" -an -c:v libx264 -crf 21 -preset fast "$4"; }
endcard() {
  txt end1 "Projektor gwiazd i galaktyki"; txt end2 "od 149 zł · dostawa 7 do 12 dni"; txt end3 "Kup teraz"
  ffmpeg -v error -y -f lavfi -i color=c=0x06081A:s=1080x1920:r=30:d=2.5 -i $LOGO -filter_complex \
  "[1]scale=640:-1[l];[0][l]overlay=(W-w)/2:620,drawtext=fontfile=$F:textfile=$T/end1.txt:fontsize=54:fontcolor=white:x=(w-text_w)/2:y=960,drawtext=fontfile=$F:textfile=$T/end2.txt:fontsize=44:fontcolor=0xC9C3FF:x=(w-text_w)/2:y=1050,drawbox=x=240:y=1200:w=600:h=130:color=0x8F7CFF@1:t=fill,drawtext=fontfile=$F:textfile=$T/end3.txt:fontsize=56:fontcolor=white:x=(w-text_w)/2:y=1240,format=yuv420p" \
  -c:v libx264 -crf 21 -preset fast "$1"
}
join() { out=$1; shift; : > "$T/l.txt"; for f in "$@"; do echo "file '$f'" >> "$T/l.txt"; done
  ffmpeg -v error -y -f concat -safe 0 -i "$T/l.txt" -c copy "$out"; }

endcard "$T/end.mp4"

# AD 01: POV, odkrywasz czego brakowało
txt h1 "POV: odkrywasz, czego
brakowało w Twoim pokoju"
vid video/GALAKTIS_VIDEO_HERO_01.mp4 5 "$(hook h1)" "$T/a1.mp4"
still crops/GALAKTIS_HERO_01_9x16.jpg 2.5 "$(hook h1)" "$T/a2.mp4"
join ads/GALAKTIS_AD_01_POV_9x16.mp4 "$T/a1.mp4" "$T/a2.mp4" "$T/end.mp4"

# AD 02: poczekaj, aż zobaczysz sufit
txt h2 "Poczekaj, aż zobaczysz sufit"
txt h2b "Wsuwasz slajd.
Gasisz światło."
still crops/GALAKTIS_UGC_01_9x16.jpg 2.5 "$(hook h2b)" "$T/b1.mp4"
vid video/GALAKTIS_VIDEO_HERO_01.mp4 5 "$(hook h2)" "$T/b2.mp4"
join ads/GALAKTIS_AD_02_SUFIT_9x16.mp4 "$T/b1.mp4" "$T/b2.mp4" "$T/end.mp4"

# AD 03: mój pokój po 22:00
txt h3 "Mój pokój po 22:00"
vid video/GALAKTIS_VIDEO_POV_01.mp4 5 "$(hook h3)" "$T/c1.mp4"
still crops/GALAKTIS_BEDROOM_01_9x16.jpg 2.5 "$(hook h3)" "$T/c2.mp4"
join ads/GALAKTIS_AD_03_PO22_9x16.mp4 "$T/c1.mp4" "$T/c2.mp4" "$T/end.mp4"

# AD 04: prezent
txt h4 "Prezent dla kogoś,
kto ma już wszystko"
still crops/GALAKTIS_GIFT_01_9x16.jpg 3 "$(hook h4)" "$T/d1.mp4"
vid video/GALAKTIS_VIDEO_HERO_01.mp4 4 "$(hook h4)" "$T/d2.mp4"
join ads/GALAKTIS_AD_04_PREZENT_9x16.mp4 "$T/d1.mp4" "$T/d2.mp4" "$T/end.mp4"

rm -rf "$T"
ls -la ads

# AD 05: przed i po (te same dwa zdjęcia, "gaszenie światła"), 0 kredytów
T=$(mktemp -d)
C9="scale=1080:1434,pad=1080:1920:0:300:color=0x06081A,setsar=1,fps=30,format=yuv420p"
printf '%s' "Mój pokój wieczorem" > $T/p1.txt
printf '%s' "Klik. I to samo miejsce." > $T/p2.txt
ffmpeg -v error -y -loop 1 -t 2.6 -i masters/GALAKTIS_BEFORE_02.png -loop 1 -t 4.4 -i masters/GALAKTIS_AFTER_02.png -filter_complex \
"[0]$C9,fade=t=out:st=2.3:d=0.3,drawtext=fontfile=$F:textfile=$T/p1.txt:fontsize=62:fontcolor=white:x=(w-text_w)/2:y=130[a];\
[1]$C9,fade=t=in:st=0:d=0.5,drawtext=fontfile=$F:textfile=$T/p2.txt:fontsize=62:fontcolor=white:x=(w-text_w)/2:y=130[b];[a][b]concat=n=2:v=1[v]" \
-map "[v]" -c:v libx264 -crf 21 -preset fast $T/p.mp4
F=$F LOGO=$LOGO
txt() { printf '%s' "$2" > "$T/$1.txt"; }
endcard "$T/end.mp4"
join ads/GALAKTIS_AD_05_PRZED_PO_9x16.mp4 "$T/p.mp4" "$T/end.mp4"
rm -rf "$T"
