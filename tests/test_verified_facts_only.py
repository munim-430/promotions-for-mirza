from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE_FILES = [
    ROOT / "README.md",
    ROOT / "PROJECT.md",
    ROOT / "VERIFIED_FACTS.md",
    ROOT / "NEXT_STEPS.md",
    *sorted((ROOT / "00_SEOJEONG_UNIVERSITY_GROUP_INSURANCE_RECOVERY_PACK").glob("*.md")),
]

FORBIDDEN = {
    "KRW 100,000,000": "obsolete DB death-benefit amount",
    "KRW 50,000,000": "obsolete DB provisional-payment amount",
    "KRW 35,000,000": "unverified Seojeong estimate",
    "KRW 70,000,000": "unverified Seojeong estimate",
    "100% payout": "unsupported guarantee",
    "100% guaranteed": "unsupported guarantee",
    "DB Insurance Primary Recovery": "closed DB recovery theory",
}


def test_no_obsolete_claims_in_active_docs():
    errors = []
    for path in ACTIVE_FILES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for token, reason in FORBIDDEN.items():
            if token in text:
                errors.append(f"{path.relative_to(ROOT)}: {token!r} ({reason})")
    assert not errors, "\n".join(errors)
