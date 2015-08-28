<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Temple Remote Control</title>
    <style>
        body {
            background-color: #eee;
        }
        button.action {
            display:block;
            margin-top: 15px;
            margin-left: auto;
            margin-right: auto;
            width: 200px;
            text-align:center;
            padding: 10px;

        }
        .color_blue {
            background-color: #0066FF;
        }
        .color_red {
            background-color: #FF3300;
        }
        .color_green {
            background-color: #33CC33;
        }
        .color_orange {
            background-color: #FF9900;
        }
        .color_purple {
            background-color: #9933FF;
        }
        .color_white {
            background-color: #FFFFFF;
        }
        .color_yellow {
            background-color: #FFFF00;
        }
        .off {
            color: #eee;
            background-color: #000000;
        }

        .notice {
            display: block;
            padding: 10px;
            margin: 20px;
            border: 1px solid #aaa;
            font-family: monospace;
            font-size: 18px;
            font-variant: small-caps;
            font-weight: 700;
        }
    </style>
</head>
<body>
<?php
// LIGHT CONTROL
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $script = $_POST["script"];
    echo "<div class=\"notice\">";
    echo "<p>";
    shell_exec("pkill python");
    echo "SCRIPT: $script";
    $cmd = "python /var/www/patterns/${script}.py -l bm2015.json > /dev/null 2>/dev/null &";
    echo "CMD: $cmd";
    echo shell_exec($cmd);
    echo "</p>";
    echo "</div>";
} ?>


<div style="margin-left:auto;margin-right:auto; width: 400px">

    <form action="templelights.php" method="POST">

        <?php
            $array = [
                "foo" => "bar",
                "bar" => "foo",
            ];

            $PATTERNS = array(
                "Rainbow Fade" => "script",
                "TEST" => "panel_test",
                "Rainbw Fade" => "rainbow_fade",
                "Burnin" => "burnin",
                "Blue" => "color_blue",
                "Green" => "color_green",
                "Orange" => "color_orange",
                "Purple" => "color_purple",
                "Red" => "color_red",
                "White" => "color_white",
                "Yellow" => "color_yellow",
                "Full Panel Fade" => "full_panel_fade",
                "Lava Lamp" => "lava_lamp",
                "Rainbow Stripes" => "rainbow_diag_stripes",
                "Slow Full Panel Fade" => "slow_full_panel_fade",
                "Spatial Stripes" => "spatial_stripes",
                "Animals" => "temple_test",
                "OFF" => "off"
            );

            foreach($PATTERNS as $key => $value) {
                echo "<button name=\"script\" class=\"action $value\" type=\"submit\" value=\"$value\">$key</button>";
            }
        ?>
    </form>

</div>
</body>
</html>
