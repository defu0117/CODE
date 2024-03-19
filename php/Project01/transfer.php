<?php
    if ( $auth == 0 ) {
        echo "<center><h2>Content Restricted</h2></center>";
    } else {
        if ( $upload == 1 )
        {
            $homedir = "/home/".$logged_in_user. "/";
            $uploaddir = "upload/";
            $target = $uploaddir . basename( $_FILES['uploaded']['name']) ;
            $uploaded_type = $_FILES['uploaded']['type'];
            $command=0;
            $ok=1;

            if ( $uploaded_type =="application/gzip" && $_POST['autoextract'] == 'true' ) {	$command = 1; }

            if ($ok==0)
            {
                echo "Sorry your file was not uploaded";
                echo "<a href='?index.php?page=upload.php' >Back to upload page</a>";
            } else {
                if(move_uploaded_file($_FILES['uploaded']['tmp_name'], $target))
                {
                    echo "<h3>The file '" .$_FILES['uploaded']['name']. "' has been uploaded.</h3><br />";
                    echo "The ownership of the uploaded file(s) have been changed accordingly.";
                    echo "<br /><a href='?page=upload.php' >Back to upload page</a>";
                    if ( $command == 1 )
                    {
                        exec("sudo tar xzf " .$target. " -C " .$homedir);
                        exec("rm " .$target);
                    } else {
                        exec("sudo mv " .$target. " " .$homedir . $_FILES['uploaded']['name']);
                    }
                    exec("/var/apache2/htdocs/update_own");
                } else {
                    echo "Sorry, there was a problem uploading your file.<br />";
                    echo "<br /><a href='?page=upload.php' >Back to upload page</a>";
                }
            }
        } else { echo "<br /><br /><h3>Home directory uploading disabled for user " .$logged_in_user. "</h3>"; }
    }
    ?>
