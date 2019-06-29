cd /Users/sbergenholtz/Applications/starfish
nameBeforeDot=HES1\ batchI
new_dir=rnascope_HES1_presentation
fileType=lif
gene_name=HES1
dirs=(NT\ HES1)
raw_image_dir=/Users/sbergenholtz/Applications/starfish/Old_analyses/rnascope_enhanced/raw
for ((i = 0; i < ${#dirs[@]}; i++))
    mkdir -p $new_dir/"${dirs[$i]}"/raw
    mkdir $new_dir/"${dirs[$i]}"/formatted
    cp "$raw_image_dir/${nameBeforeDot}.${fileType}*${dirs[$i]} *C=*.tif" "$new_dir/${dirs[$i]}/raw"
    cp "$raw_image_dir/${nameBeforeDot}.${fileType}*${dirs[$i]}*zplane*txt" "$new_dir/${dirs[$i]}/raw"
    mv "$new_dir/${dirs[$i]}/raw/*zplane_num.txt" "$new_dir/${dirs[$i]}/raw/zplane_num.txt"
done

cd $new_dir
for ((i = 0; i < ${#dirs[@]}; i++))
    zplane_num=$(cat "${dirs[$i]}/raw/zplane_num.txt")
    python3 ../formatting/2019.03.15_formatRNAscopeData_preliminaryImages.py "${dirs[$i]}/raw" "${dirs[$i]}/formatted" $new_dir "$nameBeforeDot" $fileType "${dirs[$i]}" $zplane_num
    echo "{\"version\": \"0.0.0\", \"mappings\": [{\"codeword\": [{\"c\": 0, \"r\": 0, \"v\": 1.0}], \"target\": \"$gene_name\"}]}" > "${dirs[$i]}/formatted/codebook.json"
done
