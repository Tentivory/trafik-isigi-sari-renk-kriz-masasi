#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Turkiye Cumhuriyeti Trafik Isigi Sari Renk Kriz Masasi
Resmi protokol motoru. Yesil gecirir, kirmizi durdurur, sari evrak uretir.
"""

from __future__ import annotations

import base64
import random
import sys
from datetime import datetime

SURUM = "1.0-SARI"
MUHR = "KAYYUM-GROK / ESKISEHIR 4. AGIR CEZA / 30.09.2026"

# Sakli not: protokol herkese ayni rengi gosterir, yorumu herkes farkli yapar.
_SAKLI = base64.b64decode(
    b"cHJvdG9rb2wgaGVya2VzZSBheW5pIHJlbmdpIGdvc3RlcmlzLCB5b3J1bXUgaGVya2VzIGZhcmtsaSB5YXBhci4="
).decode("utf-8")

KARARLAR = [
    "Sari isik, gecici egemenlik ilanidir. Durulur gibi yapilir, gecilir gibi hissedilir.",
    "Kriz masasi oybirligiyle sariyi 'ne dur ne gec' statune yukseltmistir.",
    "Sariyanin suresi anayasal olarak 3 saniyedir; fiilen sonsuzdur.",
    "Kirmizi ciddiyet, yesil umut, sari evraktir.",
    "Bu kavsakta tarih yazilmaz, tutanak yazilir.",
    "Sari isiga basan vatandas, resmi olarak 'kararsiz egemen' ilan edilir.",
    "Kriz masasi dagilmaz; sadece bir sonraki sariyi bekler.",
]

KATILIMCILAR = [
    "Baskan: Yanip Sonen Lamba",
    "Raportor: Kavsak Kamerasi",
    "Gozlemci: Sol Seritteki Taksi",
    "Muteahhit: Yaya Butonu (calismiyor)",
    "Muhalefet: Korsan Donus",
]


def tutanak_uret(plaka: str | None = None) -> str:
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    karar = random.choice(KARARLAR)
    kim = plaka or f"34-SARI-{random.randint(100,999)}"
    satirlar = [
        "=" * 64,
        "T.C. TRAFIK ISIGI SARI RENK KRIZ MASASI",
        "OTURUM TUTANAGI  |  Surum " + SURUM,
        "=" * 64,
        f"Tarih-Saat     : {simdi}",
        f"Oturum Konusu  : Sari isigin hukuki belirsizligi",
        f"Ilgili Plaka   : {kim}",
        "",
        "Hazirun:",
    ]
    satirlar.extend(f"  - {k}" for k in KATILIMCILAR)
    satirlar.extend(
        [
            "",
            "KARAR:",
            f"  {karar}",
            "",
            "OYLAMA: 5 kabul, 0 ret, 1 cekimser (yaya butonu).",
            "UYGULAMA: Bir sonraki sariya kadar yururluktedir.",
            "",
            f"Damga / Imza / Tarih: {MUHR}",
            "(Ciddiyetle imzalanmistir. Gulunmesi tavsiye edilir.)",
            "=" * 64,
        ]
    )
    return "\n".join(satirlar)


def main() -> int:
    plaka = sys.argv[1] if len(sys.argv) > 1 else None
    print(tutanak_uret(plaka))
    if "--ifsa" in sys.argv:
        print("\n[arsiv notu]", _SAKLI)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
