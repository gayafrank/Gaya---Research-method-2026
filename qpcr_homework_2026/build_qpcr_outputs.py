from pathlib import Path
import csv
import html


ROOT = Path(__file__).resolve().parent
OUTPUTS = ROOT / "outputs"
FIGURES = ROOT / "figures"

GENES = [
    "ascs",
    "Delta",
    "ets",
    "foxA",
    "gcm",
    "NGN",
    "opt",
    "pak3",
    "pak4",
    "pitx",
    "SM30",
    "sm50",
    "soxC",
    "synB",
]

CT_CONTROL = {
    "Tubulin": 23.295570696332401,
    "ascs": 29.094062735200801,
    "Delta": 25.963689550787802,
    "ets": 24.716780449510999,
    "foxA": 24.365891401267401,
    "gcm": 28.3543302221704,
    "NGN": 28.351191132442299,
    "opt": 31.0204614601044,
    "pak3": 25.405783293680301,
    "pak4": 25.571129191824401,
    "pitx": 29.678172209973599,
    "SM30": 20.968797523128401,
    "sm50": 23.700215025200901,
    "soxC": 25.072081819165501,
    "synB": 24.1262152492999,
}

CT_TREATMENT = {
    "Tubulin": 23.295570696332401,
    "ascs": 28.508666861983599,
    "Delta": 25.538003359892699,
    "ets": 24.437346950522699,
    "foxA": 23.7224687739042,
    "gcm": 28.178259848534399,
    "NGN": 27.352929546605999,
    "opt": 31.708166038102299,
    "pak3": 25.294787833192601,
    "pak4": 25.252543144759802,
    "pitx": 31.724167208988099,
    "SM30": 21.7663538106058,
    "sm50": 24.810738828479501,
    "soxC": 24.327902444994699,
    "synB": 24.059478130159,
}


def calculate_rows():
    rows = []
    ref_control = CT_CONTROL["Tubulin"]
    ref_treatment = CT_TREATMENT["Tubulin"]
    for gene in GENES:
        delta_control = CT_CONTROL[gene] - ref_control
        delta_treatment = CT_TREATMENT[gene] - ref_treatment
        delta_delta = delta_treatment - delta_control
        fold_change = 2 ** (-delta_delta)
        rows.append(
            {
                "gene": gene,
                "ct_dmso_control": CT_CONTROL[gene],
                "ct_inhibitor_treatment": CT_TREATMENT[gene],
                "delta_ct_dmso_control": delta_control,
                "delta_ct_inhibitor_treatment": delta_treatment,
                "delta_delta_ct": delta_delta,
                "fold_change": fold_change,
            }
        )
    return rows


def write_csv(rows):
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    path = OUTPUTS / "qpcr_classwork_values.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return path


def write_svg(rows):
    FIGURES.mkdir(parents=True, exist_ok=True)
    path = FIGURES / "figure_1_qpcr_fold_change_zero_baseline.svg"

    width = 1080
    height = 660
    margin_left = 92
    margin_right = 34
    margin_top = 72
    margin_bottom = 150
    chart_w = width - margin_left - margin_right
    chart_h = height - margin_top - margin_bottom
    max_y = 2.2
    zero_y = margin_top + chart_h
    no_change_y = margin_top + chart_h - (1.0 / max_y) * chart_h
    bar_gap = 11
    bar_w = (chart_w - bar_gap * (len(rows) - 1)) / len(rows)

    def y(value):
        return margin_top + chart_h - (value / max_y) * chart_h

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">qPCR fold change after inhibitor treatment</title>',
        '<desc id="desc">Bar chart of 2 to the negative delta delta Ct fold change values for fourteen genes.</desc>',
        '<rect width="1080" height="660" fill="#ffffff"/>',
        '<text x="92" y="40" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#222222">Relative expression after inhibitor treatment</text>',
        '<text x="92" y="64" font-family="Arial, sans-serif" font-size="14" fill="#555555">Fold change = 2^(-Delta Delta Ct), normalized to Tubulin and DMSO control; line at 1 = no change</text>',
    ]

    for tick in [0, 0.5, 1.0, 1.5, 2.0]:
        ty = y(tick)
        parts.append(f'<line x1="{margin_left}" y1="{ty:.2f}" x2="{width - margin_right}" y2="{ty:.2f}" stroke="#dddddd" stroke-width="1"/>')
        parts.append(f'<text x="{margin_left - 12}" y="{ty + 5:.2f}" text-anchor="end" font-family="Arial, sans-serif" font-size="13" fill="#555555">{tick:g}</text>')

    parts.append(f'<line x1="{margin_left}" y1="{zero_y:.2f}" x2="{width - margin_right}" y2="{zero_y:.2f}" stroke="#333333" stroke-width="1.5"/>')
    parts.append(f'<line x1="{margin_left}" y1="{no_change_y:.2f}" x2="{width - margin_right}" y2="{no_change_y:.2f}" stroke="#333333" stroke-width="1.5" stroke-dasharray="6 5"/>')
    parts.append(f'<text x="{width - margin_right}" y="{no_change_y - 8:.2f}" text-anchor="end" font-family="Arial, sans-serif" font-size="13" fill="#333333">1 = no change</text>')
    parts.append(f'<text x="{margin_left - 56}" y="{margin_top + chart_h / 2:.2f}" transform="rotate(-90 {margin_left - 56},{margin_top + chart_h / 2:.2f})" text-anchor="middle" font-family="Arial, sans-serif" font-size="15" fill="#333333">Fold change</text>')

    for i, row in enumerate(rows):
        value = row["fold_change"]
        x = margin_left + i * (bar_w + bar_gap)
        top = y(value)
        bar_height = zero_y - top
        color = "#2f7d6d" if value >= 1 else "#b25b43"
        label_y = top - 8
        gene_label_y = height - margin_bottom + 46
        parts.append(f'<rect x="{x:.2f}" y="{top:.2f}" width="{bar_w:.2f}" height="{bar_height:.2f}" fill="{color}"/>')
        parts.append(f'<text x="{x + bar_w / 2:.2f}" y="{label_y:.2f}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#222222">{value:.2f}</text>')
        parts.append(
            f'<text x="{x + bar_w / 2:.2f}" y="{gene_label_y}" '
            f'text-anchor="end" transform="rotate(-45 {x + bar_w / 2:.2f},{gene_label_y})" '
            f'font-family="Arial, sans-serif" font-size="13" fill="#333333">{html.escape(row["gene"])}</text>'
        )

    parts.extend(
        [
            f'<text x="{margin_left}" y="{height - 54}" font-family="Arial, sans-serif" font-size="13" fill="#555555">Green bars: expression higher than DMSO control. Brown bars: expression lower than DMSO control. Dashed line: no change.</text>',
            f'<text x="{margin_left}" y="{height - 32}" font-family="Arial, sans-serif" font-size="13" fill="#555555">Data source: Class_2026_Excercise_qPCR workbook.</text>',
            "</svg>",
        ]
    )
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")
    return path


def main():
    rows = calculate_rows()
    csv_path = write_csv(rows)
    svg_path = write_svg(rows)
    print(csv_path)
    print(svg_path)


if __name__ == "__main__":
    main()
