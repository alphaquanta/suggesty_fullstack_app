import { Component, Input, OnInit, Output } from '@angular/core';
import { trackItem } from '../searchbox/searchbox.component';


@Component({
  selector: 'app-track-item',
  templateUrl: './track-item.component.html',
  styleUrls: ['./track-item.component.scss'],
  
})
export class TrackItemComponent implements OnInit{
 
  isPlaying = false;
  icon_reference = "play_arrow";
  private audio = new Audio()
  
  @Input()
  track:trackItem =
  {
    "album_image_url":"",
    "artist":"",
    "preview_url": null,
    "track":""
  }
  constructor() { 

  }

  ngOnInit(): void {  
    this.audio.src = this.track.preview_url ?? "";
    this.audio.addEventListener("ended", (listener) => this.playFinished(listener))
  }

  public playPreview(){
    console.log(this.isPlaying)
    if(!this.track.preview_url)
    return;
    if(this.audio.readyState <3)
    {
      this.audio.load();
    }
    if(this.isPlaying)
    {
      console.log("stopped")
      this.audio.pause();
      this.isPlaying=false;
      this.icon_reference = "play_arrow";
    }
    else
    {
      console.log("started")
    this.isPlaying = true
    this.icon_reference = "pause"
    this.audio.play();
    }
  }

  public playFinished(event:Event)
  {
    this.audio.currentTime = 0;
    this.icon_reference = "play_arrow"
    this.isPlaying = false;
    console.log("Preview playing finished")
  }


}
